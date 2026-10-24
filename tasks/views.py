from django.shortcuts import render
from django.http import HttpResponse

def Home(requests):
    context = {
        "name":"Akhilesh",
        "course":"Web development",
        "hours":30,
        "tasks": ["Learn Django", "Build a website", "Practice CSS"],
    }
    return render(requests,"tasks/home.html",context)

def About(request):
    return HttpResponse("this is my about page")

def Contact(request):
    return HttpResponse("This is contact page")

def Greetings(request):
    name = request.GET.get("name","")
    return HttpResponse(f"Hello {name}")

def Profile(request):
    name = request.GET.get("name","")
    occupation = request.GET.get("occupation","")
    return HttpResponse(f"name is {name} and occupation is {occupation}")