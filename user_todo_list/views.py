from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetForm, PasswordResetView, PasswordResetDoneView
from .models import Task
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class Login(LoginView):
    pass
    # template_name = 'login'

class Logout(LogoutView):
    pass
    # template_name = ''

class RecoveryPassword(PasswordResetForm):
    pass

class TaskList(LoginRequiredMixin, ListView):
    model = Task


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['name', 'priority']
    success_url = reverse_lazy('task-list')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        self.object = form.save()
        return super(TaskCreate, self).form_valid(form)

class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['name', 'priority']
    success_url = reverse_lazy('task-list')

class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = reverse_lazy('task-list')

def check_task(request, pk):
    task = Task.objects.get(pk=pk)
    if not task.done:
        task.done = True
    task.save()
    return redirect('task-list')
