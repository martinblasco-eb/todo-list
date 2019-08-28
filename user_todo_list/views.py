from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import TemplateView, LoginView, LogoutView, PasswordResetForm, PasswordResetView, PasswordResetDoneView
from .models import Task
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from eventbrite import Eventbrite


# Create your views here.

class Login(LoginView):
    pass

class Logout(LogoutView):
    pass

class RecoveryPassword(PasswordResetForm):
    pass

class EventList(TemplateView):

    template_name='event_list.html'

    def get_context_data(self,**kwargs):
        content_data = super().get_context_data(**kwargs)
        content_data['events_list'] = self.get_events()
        return content_data

    def get_events(self):
        social = self.request.user.social_auth.all()[0]
        eventbrite = Eventbrite(social.access_token)
        events = eventbrite.get('/users/me/events')['events']
        return events

    def get_queryset(self):
        pass
        # return Event.objects.filter(user=self.request.user)

class TaskList(LoginRequiredMixin, ListView):

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


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
