from django.urls import path 
from . import views

urlpatterns = [
    path("",views.Home),
    path("about/",views.About),
    path("contact/",views.Contact),
    path("greetings/",views.Greetings),
    path("profile/",views.Profile,name='profile'),
    path("tasks/", views.task_list, name='task_list')
]

# Question: What are the components of Django's path() function?

#  Django's path() function accepts a URL route, a view callable,-
#  and optional keyword arguments such as name.

# path("tasks/", views.task_list, name="task_list")

# "tasks/" defines the URL route.
# views.task_list references the view function.
# name="task_list" assigns a name to the URL pattern.