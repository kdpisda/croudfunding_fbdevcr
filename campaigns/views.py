from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from .models import Campaign


# Create your views here.
def login_view(request):
    if request.method == "GET":
        return render(request, "login.html")
    else:
        username = request.POST.get("username")
        passsword = request.POST.get("password")
        user = authenticate(username=username, password=passsword)

        print(user)
        if user is not None:
            login(request, user)
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


def new_campaign(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            return render(request, "new_campaign.html")
        else:
            title = request.POST.get("title")
            description = request.POST.get("description")
            amount = request.POST.get("amount")
            new_campaign = Campaign()
            new_campaign.title = title
            new_campaign.description = description
            new_campaign.amount = amount
            new_campaign.supporting_document = request.FILES.get(
                "supporting_document")
            new_campaign.user = request.user
            new_campaign.save()
            # TODO: Banana hai
            return redirect('/campaigns')
    else:
        return redirect('/login')