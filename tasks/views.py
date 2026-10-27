from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Task,Contact

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
    errors = []
    name = ''
    phone = ''

    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        phone = request.POST.get("phone", "").strip()

        # Server-side validation

        if not name:
            errors.append("Name is required.")
        elif not phone:
            errors.append("Phone number is required")
        elif len(name) > 15:
            errors.append("name cannot exceed 15 characters.")
        elif len(phone) > 10:
            errors.append("name cannot exceed 10 characters.")

        # Save only when there are no validation errors

        if not errors:
            Contact.objects.create(
                name=name,
                phone=phone
            )

            return redirect("contact")

    context = {
        'errors': errors,
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