from django.urls import path

# when you use views, you have to import it. Because it's in the same
# directory, you can use '.' to import it.
from . import views

urlpatterns = [
   path("", views.index, name="index"),
   path("andrew", views.andrew, name="andrew"),
   path("david", views.david, name="david"),
   path("<str:name>", views.greet, name="greet")
]
