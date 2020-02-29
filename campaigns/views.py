from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def login(request):
    return render(request, "login.html")
    # return HttpResponse("Login World")


def register(request):
    return HttpResponse("Registr World")