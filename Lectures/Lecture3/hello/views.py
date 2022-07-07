from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    #HttpResponse is a special function created by Django!
    # use render if you don't just wanna render text, but a full html file
    return render(request, "hello/index.html") 

def andrew(request):
    return HttpResponse("Hello, Andrew!")

def greet(request, name):
    # You are allowed to add arbitrary Python logic!
    # if you can do it in Python, Django will allow you to incorporate it
    # in the response.
    # Optional 3rd arg for render: the context. It is all the info you would
    # like to provide to the template. All the vars you want the template to
    # have access to.
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
        })
