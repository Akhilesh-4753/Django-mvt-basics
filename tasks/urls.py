from django.urls import path 
from . import views

urlpatterns = [
    path("",views.Home),
    path("about",views.About),
    path("contact",views.Contact),
    path("greetings",views.Greetings),
    path("profile",views.Profile)
]