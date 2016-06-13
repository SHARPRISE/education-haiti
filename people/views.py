from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.http import HttpRequest
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from people.models import User, Mentor, Mentee
from people.forms import LoginForm, MentorLoginForm, RegisterForm, MentorRegisterForm, ChangeMentorProfile

from datetime import datetime
from hashlib import sha1
# Create your views here.


#normal register for mentees
def register(request, template="register.html"):
    if request.user.is_authenticated():
        # TODO home page
        return redirect("people:dashboard")

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(
                # username
                form.cleaned_data["username"],
                # email
                form.cleaned_data["email"],
                )

            new_user.set_password(form.cleaned_data["password"])
            # TODO : implementation of email validation
            new_user.is_active = True
            # rank
            new_user.rank = form.cleaned_data["rank"]
            new_user.save()
            new_mentee = Mentee(user=new_user)

            url = "<h2><a href='/people/login'>Login</a></h2>"
            go_back = "<h1>successfully registered, go back to login page:</h1> <br /> </h1>"
            return HttpResponse(go_back + url)
    else:
        form = RegisterForm()
    return render(request, template, {"form":form,
                                      'title': 'Mentee Register'})


#register for mentor
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


#normal login for mentees
def login_view(request, template="login.html"):
    if request.user.is_authenticated():
        # TODO redirect to home page
        return redirect("people:dashboard")

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(username=username, password=password)
        if user is not None:
            # the password verified for the user
            if user.is_active:
                login(request, user)
                if user.rank == 'B':
                    return redirect("people:dashboard")
                else:
                    url = "<h2><a href='/people/mentor_login'>Back to Mentor Login &raquo</a></h2>"
                    bad_rank = "<h1>Wrong Login</h1>" \
                               "<br />" \
                               "<h2>You are trying to connect to the Mentee page with a Mentor account." \
                               "<b>This is not possible!!! </b>" \
                               "Please go back and login on the Mentor login page.</h2>"
                    logout(request)
                    return HttpResponse(bad_rank + url)
                # TODO redirect to home page
            else:
                return HttpResponse("account inactive")
        else:
            return HttpResponse("username/password incorrect")
            # the authentication system was unable to verify the username and passwor
    else:
        pass
    form = LoginForm()
    return render(request, template, {"form" : form,
                                      "title" : 'Mentee Login'})


#custom login view for mentors
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
                if user.rank == 'A':
                    return redirect("people:dashboard")
                else:
                    url = "<h2><a href='/people/login'>Back to Mentee Login &raquo</a></h2>"
                    bad_rank = "<h1>Wrong Login</h1>" \
                               "<br />" \
                               "<h2>You are trying to connect to the Mentor page with a Mentee account." \
                               "<b>This is not possible!!! </b>" \
                               "Please go back and login on the Mentee login page.</h2>"
                    logout(request)
                    return HttpResponse(bad_rank + url)
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

#    form = MentorLoginForm(request.POST or None)
#	next_url = request.GET.get('next')
#	if form.is_valid():
#		email = form.cleaned_data['email']
#		password = form.cleaned_data['password']
#       graduating or university = ...
#		user = authenticate(email=email, password=password)
#		if user is not None:
#			login(request, user)
#			if next_url is not None:
#				return HttpResponseRedirect(next_url)
#			return HttpResponseRedirect("/admin")
#	action_url = reverse("login")
#	title = "Login"
#	submit_btn = title
#	submit_btn_class = "btn-success btn-block"
#	context = {
#		"form": form,
#		"action_url": action_url,
#		"title": title,
#		"submit_btn": submit_btn,
#		"submit_btn_class": submit_btn_class,
#		}
#	return render(request, "accounts/account_login.html", context)
# DON'T WORRY ONLY THE LOGIC IS NEEDED, this is just a personal code snippet

def mentor_update(request, template='mentor_profile.html'):
    if request.user.is_authenticated():
        form = ChangeMentorProfile(request.POST or None)
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
        context = {
            'form': form
        }
        return render(request, template, context)

def logout_view(request):
    logout(request)
    return redirect("index")

def dashboard(request):
        "Renders the dashboard page"
        assert isinstance(request, HttpRequest)
        return render(
            request,
            'dashboard.html',
            context_instance=RequestContext(request,
            {
                'title': 'Dashboard',
                'year': datetime.now().year,
                'date': datetime.now().date,
            })
        )

def mentor_profile(request):
    "renders the dashboard page"
    assert isinstance(request, HttpRequest)
    form = ChangeMentorProfile()
    return render(
        request,
        'mentor_profile.html',
        context_instance=RequestContext(request,
        {
            'title': 'Mentor Profile',
            'form': form,
        })

    )
