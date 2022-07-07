from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("andrew", views.andrew, name="andrew"),
    path("<str:name>", views.greet, name="greet")
]
