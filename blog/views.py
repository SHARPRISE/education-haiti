from django.shortcuts import render, render_to_response, HttpResponseRedirect, get_object_or_404
from django.http import HttpRequest, HttpResponse, Http404
from django.template import RequestContext
from datetime import datetime
from .models import SuccessStory
from programs.models import Programs

# HomePage view
def index(request):
    # Gets the success stories
    story = SuccessStory.objects.filter(featured=True).order_by('top_story', 'created').reverse()
    "Renders the home page"
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'index.html',
        {'stories': story},
        context_instance=RequestContext(request,
        {
            'title': 'Home',
            'year': datetime.now().year,
            'date': datetime.now().date,
        })
    )

def get_homepage(request):
    return render(request, 'index.html')


# Success Stories page view
def success_blog(request):
    # Gets the success stories
    story = SuccessStory.objects.filter(published=True).order_by('top_story', 'featured', 'created').reverse()
    "Renders the success stories page"
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'success-stories.html',
        {'stories': story},
        context_instance=RequestContext(request,
        {
            'title': 'Our Success Stories',
            'year': datetime.now().year,
            'date': datetime.now().date(),
        })
    )
# I'm adding this comment to debug the Heroku deployment

# Success Stories slug thingy
def story(request, slug):
    story = get_object_or_404(SuccessStory, slug=slug)
    title = story.title
    # return the rendered article
    return render(request, 'success.html', {'story': story, 'title': title})


# Guides page view
def guides(request):
    "renders the guides page"
    assert isinstance(request,HttpRequest)
    return render(
        request,
        'guides.html',
        context_instance=RequestContext (request,
        {
            'title': 'Recommended Resources'
        })
    )

def signup(request):
    return render(request, 'apply.html')

def handler404(request):
    response = render_to_response('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response


def handler500(request):
    response = render_to_response('500.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response
