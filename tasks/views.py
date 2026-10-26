from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Task

def Home(requests):

    tasks = [
        "Learn Django URLs",
        "Understand views",
        "Build a template",
    ]

    context = {
        "tasks": tasks,
        "is_student": True,
    }

    return render(requests,"tasks/home.html",context)

def About(request):

    course = ["developer","designer","prompt engineer"]

    return render(request,"tasks/about.html",{"course": course})

def Contact(request):
    name = ''
    phone = ''

    if request.method == 'POST':
        name = request.POST.get('name', '')
        phone = request.POST.get('phone', '')

        print("Name:", name)
        print("Phone:", phone)

    context = {
        'name': name,
        'phone': phone
    }

    return render(request, "tasks/contact.html", context)

def Greetings(request):
    name = request.GET.get("name","")
    return HttpResponse(f"Hello {name}")

def Profile(request):
    name = request.GET.get("name","")
    occupation = request.GET.get("occupation","")
    return HttpResponse(f"name is {name} and occupation is {occupation}")

def task_list(request):
    errors = []
    title = ""
    description = ""

    if request.method == "POST":
        title = request.POST.get("title", "").strip()
        description = request.POST.get("description", "").strip()

        # Server-side validation

        if not title:
            errors.append("Title is required.")
        elif not description:
            errors.append("Description is required")
        elif len(title) > 200:
            errors.append("Title cannot exceed 200 characters.")

        # Save only when there are no validation errors
        if not errors:
            Task.objects.create(
                title=title,
                description=description
            )

            return redirect("task_list")

    context = {
        "errors": errors,
        "title": title,
        "description": description,
    }

    return render(
        request,
        "tasks/create_task.html",
        context
    )