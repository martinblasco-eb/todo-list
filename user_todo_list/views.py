from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from .models import Task
from django.core.urlresolvers import reverse_lazy


# Create your views here.

class TaskList(ListView):
    model = Task

class TaskCreate(CreateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('task-list')

class TaskUpdate(UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('task-list')
