from django.shortcuts import render, redirect, get_object_or_404
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
        return redirect("feed:home")

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(
                # email
                form.cleaned_data["email"],
                # username
                form.cleaned_data["username"],
                )

            new_user.set_password(form.cleaned_data["password"])
            # TODO : implementation of email validation
            new_user.is_active = False
            # rank
            new_user.rank = form.cleaned_data["rank"]
            print(form.cleaned_data["rank"])
            
            new_user.save()

            return redirect("blog:index")
    else:
        form = RegisterForm()
    return render(request, template, {"form":form})

def login_view(request, template="login.html"):
    if request.user.is_authenticated():
        # TODO redirect to home page
        return redirect("feed:home")

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(username=username, password=password)
        if user is not None:
            # the password verified for the user
            if user.is_active:
                login(request, user)
                # TODO redirect to home page
                return redirect("feed:home")
            else:
                # account disabled or inactive
                pass
        else:
            print("password incorrect")
            # the authentication system was unable to verify the username and password
            pass
    else:
        pass
    form = LoginForm()
    return render(request, template, {"form" : form})

def activate(request, template="activate.html"):
    if request.method == "POST":
        form = ActivationForm(request.POST)
        if form.is_valid():
            user = get_or_404(User, email = form.cleaned_data["email"])
            if user.activation_key != form.cleaned_data["activation_key"]:
                return render(request, template, {"form":form})
            user.is_active = True
            user.save()
    else:
        form = ActivationForm()
    return render(request, template, {"form" : form})

def logout_view(request):
    logout(request)
    return redirect("blog:index")
