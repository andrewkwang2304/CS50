from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def index(request):
    now = datetime.datetime.now()
    # Here, we must add some logic to see if it's Jan 1.
    return render(request, "newyear/index.html", {
        "newyear": now.month == 1 and now.day == 1
        })
