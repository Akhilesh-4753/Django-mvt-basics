from django.shortcuts import render
from django.http import HttpResponse

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
    return HttpResponse("This is contact page")

def Greetings(request):
    name = request.GET.get("name","")
    return HttpResponse(f"Hello {name}")

def Profile(request):
    name = request.GET.get("name","")
    occupation = request.GET.get("occupation","")
    return HttpResponse(f"name is {name} and occupation is {occupation}")