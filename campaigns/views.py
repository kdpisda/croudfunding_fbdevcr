from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    else:
        # TODO: Kuchh karenge
        return render(request, "login.html")


def register(request):
    return render(request, "register.html")