from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.http import HttpRequest
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout

from people.models import User, Mentor, ToDo
from blog.models import SuccessStory
from people.forms import MentorLoginForm, MentorRegisterForm, MentorUpdateForm, ToDoForm, ToDoCompletionForm
from blog.forms import AddStoryForm

from datetime import datetime
# Create your views here.


# register for mentor
def register_mentor(request, template="register_mentor.html"):
    if request.user.is_authenticated():
        return redirect("people:dashboard")
    if request.method == "POST":
        form = MentorRegisterForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(
                form.cleaned_data["username"],
                form.cleaned_data["email"],
            )
        new_user.set_password(form.cleaned_data["password"])
        new_user.undergrad_college = form.cleaned_data["undergrad_college"]
        new_user.rank = 'A'
        new_user.is_active = True
        new_user.save()
        new_mentor = Mentor(user=new_user, undergrad_college=form.cleaned_data["undergrad_college"])
        new_mentor.save()
        url = "<h2><a href='/people/mentor_login'>Login</a></h2>"
        go_back = "<h1>successfully registered, go back to login page:</h1> <br /> </h1>"
        return HttpResponse(go_back + url)
    else:
        form = MentorRegisterForm()
    return render(request, template, {"form":form,
                                      'title': 'Mentor Register'})


# custom login view for mentors
def mentor_login(request, template="mentor_login.html"):
    if request.user.is_authenticated():
        # TODO redirect to home page
        return redirect("people:dashboard")
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        undergrad_college = request.POST["undergrad_college"]

        user = authenticate(username=username, password=password, undergrad_college=undergrad_college)
        if user is not None:
            # the password verified for the user
            if user.is_active:
                login(request, user)
                return redirect("people:dashboard")
            else:
                return HttpResponse("account inactive")
        else:
            return HttpResponse("username/password/university incorrect")
    # the authentication system was unable to verify the username and password
    else:
        pass
    form = MentorLoginForm()
    return render(request, template, {'form': form,
                                      'title': 'Mentor Login'})


def mentor_update(request, template='mentor_profile.html'):
    if request.user.is_authenticated():
        form = MentorUpdateForm(request.POST or None)
        online_user = request.user
        mentor = online_user.mentor
        if form.is_valid():
            mentor.biography = form.cleaned_data['biography']
            mentor.grad_college = form.cleaned_data['grad_college']
            mentor.majors = form.cleaned_data['majors']
            mentor.interests = form.cleaned_data['interests']
            mentor.residency = form.cleaned_data['residency']
            mentor.phone = form.cleaned_data['phone']
            mentor.current_status = form.cleaned_data['current_status']
            mentor.school_haiti = form.cleaned_data['school_haiti']
            mentor.first_name = form.cleaned_data['first_name']
            mentor.last_name = form.cleaned_data['last_name']
            mentor.picture = form.cleaned_data['picture']
            mentor.save()
            return redirect("people:dashboard")
        context = {
            'form': form
        }
        return render(request, template, context)


def todo_completion(request, template='dashboard.html'):
    if request.user.is_authenticated():
        form = ToDoCompletionForm(request.POST or None)
        online_user = request.user.username
        if form.is_valid():
            todos = ToDo.objects.filter(author=online_user).all()
            for el in todos:
                el.completion = True
                el.save()
                return redirect("people:dashboard")
        context = {
            'form': form
        }
        return render(request, template, context)


def add_todo(request, template='dashboard.html'):
    form = ToDoForm(request.POST or None)
    online_user = request.user.username
    if form.is_valid():
        new_todo = ToDo(author=online_user)
        new_todo.subject = form.cleaned_data['subject']
        new_todo.expires = form.cleaned_data['expires']
        new_todo.save()
        return redirect("people:dashboard")
    context = {
        'form': form
    }
    return render(request, template, context)


def remove_todo(request, template='dashboard.html'):
    online_user = request.user.username
    todos = ToDo.objects.filter(author=online_user, completion=True).all()
    for el in todos:
        el.delete()
        return redirect("people:dashboard")
    return render(request, template)


def add_story(request, template='add_story.html'):
    form = AddStoryForm(request.POST or None)
    online_user = request.user
    mentor_first_name = online_user.mentor.first_name
    mentor_last_name = online_user.mentor.last_name
    if form.is_valid():
        new_story = SuccessStory(author=mentor_first_name + ' ' + mentor_last_name)
        new_story.title = form.cleaned_data['title']
        new_story.description = form.cleaned_data['description']
        new_story.content = form.cleaned_data['content']
        new_story.slug = form.cleaned_data['slug']
        new_story.published = form.cleaned_data['published']
        new_story.created = datetime.now().date()
        new_story.article_picture = form.cleaned_data['article_picture']
        new_story.save()
        return redirect("people:dashboard")
    context = {
        'form': form
    }
    return render(request, template, context)


def logout_view(request):
    logout(request)
    return redirect("index")


def dashboard(request):
        """Renders the dashboard page"""
        todo = ToDo.objects.all()
        for el in todo:
            ToDo.auto_delete_check(el)
        assert isinstance(request, HttpRequest)
        add_todo_form = ToDoForm
        complete_todo_form = ToDoCompletionForm
        return render(
            request,
            'dashboard.html',
            {'todos': todo},
            context_instance=RequestContext(request,
            {
                'title': 'Dashboard',
                'form_add': add_todo_form,
                'form_complete': complete_todo_form,
                'year': datetime.now().year,
                'date': datetime.now().date,
            })
        )


def mentor_profile(request):
    "renders the dashboard page"
    assert isinstance(request, HttpRequest)
    form = MentorUpdateForm()
    return render(
        request,
        'mentor_profile.html',
        context_instance=RequestContext(request,
        {
            'title': 'Mentor Profile',
            'form': form,
        })

    )


def new_story(request):
    """renders the new story page"""
    assert isinstance(request, HttpRequest)
    form = AddStoryForm()
    return render(
        request,
        'add_story.html',
        context_instance=RequestContext(request,
                                        {
                                            'title': 'New Success Story',
                                            'form': form,
                                        })
    )


