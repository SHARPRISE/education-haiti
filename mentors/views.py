from django.shortcuts import render, HttpResponseRedirect, redirect, get_object_or_404
from django.template import RequestContext
from datetime import datetime
from django.http import HttpRequest
from people.models import User

# Create your views here.


def our_mentors(request):
    #Gets the success stories
    user = User.objects.filter(rank='mentor')
    "Renders the our mentors page"
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'our_mentors.html',
        {'users': user},
        context_instance=RequestContext(request,
        {
            'title': 'Our Mentors',
            'year': datetime.now().year,
            'date': datetime.now().date(),
        })
    )