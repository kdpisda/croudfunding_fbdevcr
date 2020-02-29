from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout


# Create your views here.
def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    else:
        username = request.POST.get("username")
        passsword = request.POST.get("password")
        user = authenticate(username=username, passsword=passsword)

        if user is not None:
            print("Valid User")
            return redirect('/profile')
        else:
            print("Farzi hai")
            return render(request, "login.html")


def register(request):
    return render(request, "register.html")


def profile(request):
    if request.user.is_authenticated:
        return render(request, "profile.html")
    else:
        return redirect("/login")


def logout_view(request):
    logout(request)
    return redirect('/login')