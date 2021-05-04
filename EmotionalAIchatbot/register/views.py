from urllib import request

from django.shortcuts import render , redirect
from .forms import RegisterForm


# Create your views here.

def register(response):

    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect("/login")
    else:
        form = RegisterForm()

    if not response.user.is_authenticated:
        return render(response, "register/register.html", {"form":form})

    else:
        return redirect('/profile')

