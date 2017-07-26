from django.shortcuts import render, HttpResponseRedirect, redirect, get_object_or_404
from django.template import RequestContext
from datetime import datetime
from django.http import HttpRequest
from people.models import Mentor

# Create your views here.

def become_a_mentor(request):
    return render(request, 'mentor_application.html')

def our_mentors(request):
    #Gets the success stories
    mentor = Mentor.objects.all()
    "Renders the our mentors page"
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'mentors.html',
        {'mentors': mentor},
        context_instance=RequestContext(request,
        {
            'title': 'Our Mentors',
            'year': datetime.now().year,
            'date': datetime.now().date(),
        })
    )

def mentors(request):
    mentor = Mentor.objects.all()
    assert isinstance(request, HttpRequest)
    return render(request, 'mentors.html', {'mentors': mentor})
