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

class TaskList(LoginRequiredMixin, TemplateView):

    template_name='task_list.html'

    def get_context_data(self, **kwargs):
        token = self.request.user.social_auth.all()[0]
        context = super(TaskList, self).get_context_data(**kwargs)
        context['event_id'] = self.kwargs['event_id']
        context['tasks'] = Task.objects.filter(event=self.kwargs['event_id'])
        return context


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['name', 'priority']

    def get_success_url(self):
        return reverse_lazy('task-list', kwargs={'event_id': self.kwargs['event_id']})

    def form_valid(self, form):
        form.instance.event = self.kwargs['event_id']
        form.instance.user = self.request.user
        self.object = form.save()
        return super(TaskCreate, self).form_valid(form)

class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['name', 'priority']

    def get_success_url(self):
        return reverse_lazy('task-list', kwargs={'event_id': self.kwargs['event_id']})

class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task

    def get_success_url(self):
        return reverse_lazy('task-list', kwargs={'event_id': self.kwargs['event_id']})

def check_task(request, event_id, pk):
    task = Task.objects.get(pk=pk)
    if not task.done:
        task.done = True
    task.save()
    return redirect('task-list', event_id=event_id)
