from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "hello/index.html") 

def andrew(request):
    return HttpResponse("Hello, Andrew!")

def david(request):
    return HttpResponse("Hello, David!")

def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
        })
