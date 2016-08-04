from django.shortcuts import render, HttpResponseRedirect, redirect, get_object_or_404
from django.http import Http404
from django.http import HttpRequest
from django.http import HttpResponse
from django.template import RequestContext
from datetime import datetime
from .models import SuccessStory
from programs.models import Programs


# HomePage view
def index(request):
    # Gets the success stories
    story = SuccessStory.objects.filter(published=True).order_by('created')
    program = Programs.objects.filter(expired_final=False)
    "Renders the home page"
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'index.html',
        {'stories': story, 'programs': program},
        context_instance=RequestContext(request,
        {
            'title': 'Home',
            'year': datetime.now().year,
            'date': datetime.now().date,
        })
    )


# Success Stories page view
def success_blog(request):
    # Gets the success stories
    story = SuccessStory.objects.filter(published=True).reverse()
    "Renders the success stories page"
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'success_blog.html',
        {'stories': story},
        context_instance=RequestContext(request,
        {
            'title': 'Our Success Stories',
            'year': datetime.now().year,
            'date': datetime.now().date(),
        })
    )


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