from django.shortcuts import render, HttpResponseRedirect, redirect, get_object_or_404
from django.http import Http404
from django.http import HttpRequest
from django.http import HttpResponse
from django.template import RequestContext
from datetime import datetime

from .forms import AddProgramForm
from .models import Programs
# Create your views here.


def add_program(request, template='add_program.html'):
    form = AddProgramForm(request.POST or None)
    if form.is_valid():
        new_program = Programs()
        new_program.name = form.cleaned_data['name']
        new_program.location = form.cleaned_data['location']
        new_program.description = form.cleaned_data['description']
        new_program.slug = form.cleaned_data['slug']
        new_program.details = form.cleaned_data['details']
        new_program.start_date = form.cleaned_data['start_date']
        new_program.end_date = form.cleaned_data['end_date']
        new_program.phone_contact = form.cleaned_data['phone_contact']
        new_program.email_contact = form.cleaned_data['email_contact']
        new_program.deadline = form.cleaned_data['deadline']
        new_program.picture = form.cleaned_data['picture']
        new_program.save()
        return redirect("people:dashboard")
    context = {
        'form': form
    }
    return render(request, template, context)


def add_program_page(request):
    assert isinstance(request, HttpRequest)
    form = AddProgramForm()
    return render(
        request,
        'add_program.html',
        context_instance=RequestContext(request,
                                        {
                                            'title': 'Add A New Program',
                                            'year': datetime.now().year,
                                            'date': datetime.now().date,
                                            'form':form,
                                        })
    )


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
            'title': 'Programs',
            'year': datetime.now().year,
            'date': datetime.now().date,
        })
    )


def about(request):
    "Renders the programs page"
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'about.html',
        context_instance=RequestContext(request,
        {
            'title': 'About',
            'year': datetime.now().year,
            'date': datetime.now().date,
        })
    )


def contact(request):
    "Renders the contact page"
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'contact.html',
        context_instance=RequestContext(request,
        {
            'title': 'Contact',
            'year': datetime.now().year,
            'date': datetime.now().date,
        })
    )
