from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages

from .models import Task,Contact
from .forms import TaskForm

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

def Contacts(request):
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
            errors.append("number cannot exceed 10 characters.")

        # Save only when there are no validation errors

        if not errors:
            Contact.objects.create(
                name=name,
                phone=phone
            )

            return redirect("Contactss")

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
    
    if request.method == "POST":
        
        form = TaskForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("task_list")
    else:
        form = TaskForm()

    context = {
        "form": form,
    }

    return render(request, "tasks/create_task.html", context)

def show_tasks(request):
    
    tasks = Task.objects.all().order_by('-created_at')

    context = {
    'tasks': tasks,
    }

    return render(request, 'tasks/showtask.html', context)

def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)

        if form.is_valid():
            form.save()
            messages.success(request, "Task saved successfully!")
            return redirect('show_tasks')

    else:
        form = TaskForm(instance=task)

    context = {
        'form': form,
        'task': task,
    }

    return render(request, 'tasks/edit_task.html', context)

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == "POST":
        task.delete()
        messages.success(request, "Task deleted successfully!")

    return redirect('show_tasks')

def toggle_completed(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == "POST":
        task.completed = not task.completed
        task.save(update_fields=['completed'])

        if task.completed:
            messages.success(request, "Task marked as completed!")
        else:
            messages.success(request, "Task marked as pending!")

    return redirect('show_tasks')