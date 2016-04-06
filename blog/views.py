from django.shortcuts import render, HttpResponseRedirect, redirect
from django.http import Http404
from django.http import HttpRequest
from django.http import HttpResponse
from django.template import RequestContext
from datetime import datetime

#HomePage view
def index(request):
    "Renders the home page"
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'index.html',
        context_instance = RequestContext(request,
        {
            'title':'Home',
            'year':datetime.now().year,
            'date':datetime.now().date,
        })
    )