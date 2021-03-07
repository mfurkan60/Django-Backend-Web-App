from django.shortcuts import render
from django.http import HttpResponse
from .models import Todos

# Create your views here.
def index(request):
    todo_list = Todos.objects.all()
    return render(request , "todo_app/index.html",{'todo_list':todo_list})


def about(request):
    return render(request , "todo_app/about.html")  


def create(request):
    return render(request , "todo_app/create.html") 

