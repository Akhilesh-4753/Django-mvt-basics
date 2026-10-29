from django.urls import path
from . import views

urlpatterns = [
    path("", views.Home, name="home"),
    path("about/", views.About, name="about"),
    path("contact/", views.Contacts, name="Contactss"),
    path("greetings/", views.Greetings, name="greetings"),
    path("profile/", views.Profile, name="profile"),

    # Create task
    path("tasks/", views.task_list, name="task_list"),

    # Show all tasks
    path("showtasks/", views.show_tasks, name="show_tasks"),

    # Edit task
    path("edit-task/<int:task_id>/", views.edit_task, name="edit_task"),

    # Delete task
    path("delete-task/<int:task_id>/", views.delete_task, name="delete_task"),

    # Update completed/pending status
    path(
        "toggle-completed/<int:task_id>/",
        views.toggle_completed,
        name="toggle_completed",
    ),
]