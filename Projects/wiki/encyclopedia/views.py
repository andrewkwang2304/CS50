from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


#def renderentry(request, entry):
#    return render(request, "entries/<str:entry>")
