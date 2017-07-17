from django.shortcuts import render, HttpResponseRedirect, redirect, get_object_or_404
from django.http import Http404
from django.http import HttpRequest
from django.http import HttpResponse
from django.template import RequestContext
from datetime import datetime

from .forms import AddProgramForm
from .models import Programs
# Create your views here.

def programs(request):
    "Renders the programs page"
    open_program = Programs.objects.all().filter(expired_deadline=False)
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'programs.html',
        {'open_programs': open_program},
        context_instance=RequestContext(request,
        {
            'title': 'Our Programs',
            'year': datetime.now().year,
            'date': datetime.now().date,
        })
    )
