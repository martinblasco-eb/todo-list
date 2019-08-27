from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Task
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect


# Create your views here.

class TaskList(ListView):
    model = Task

class TaskCreate(CreateView):
    model = Task
    fields = ['name', 'priority']
    success_url = reverse_lazy('task-list')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        self.object = form.save()
        return super(TaskCreate, self).form_valid(form)

class TaskUpdate(UpdateView):
    model = Task
    fields = ['name', 'priority']
    success_url = reverse_lazy('task-list')

class TaskDelete(DeleteView):
    model = Task
    success_url = reverse_lazy('task-list')

def check_task(request, pk):
    task = Task.objects.get(pk=pk)
    if not task.done:
        task.done = True
    task.save()
    return redirect('task-list')
