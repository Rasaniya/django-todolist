from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo
from .forms import *

# Create your views here.
def index(request):
    todos = Todo.objects.all()
    form = TodoForm()

    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    return render(request, 'index.html', {'todos': todos, 'form':form})