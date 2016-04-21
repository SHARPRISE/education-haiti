from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from people.models import User
from people.forms import LoginForm, RegisterForm

from datetime import datetime
from hashlib import sha1
# Create your views here.

def register(request, template="register.html"):
    if request.user.is_authenticated():
        # TODO home page
        return redirect("index")

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
            url = "<h2><a href='/people/login'>Login</a></h2>"
            go_back = "<h1>successfully registered, go back to login page:</h1> <br /> </h1>"
            return HttpResponse(go_back + url)
    else:
        form = RegisterForm()
    return render(request, template, {"form":form})

#normal login for mentees
def login_view(request, template="login.html"):
    if request.user.is_authenticated():
        # TODO redirect to home page
        return redirect("index")

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(username=username, password=password)
        if user is not None:
            # the password verified for the user
            if user.is_active:
                login(request, user)
                # TODO redirect to home page
                return redirect("index")
            else:
                return HttpResponse("account inactive")
        else:
            return HttpResponse("username/password incorrect")
            # the authentication system was unable to verify the username and passwor
    else:
        pass
    form = LoginForm()
    return render(request, template, {"form" : form})

#custom login view for mentors
#def mentor_login(request):
#    form = LoginForm(request.POST or None)
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


def logout_view(request):
    logout(request)
    return redirect("index")
