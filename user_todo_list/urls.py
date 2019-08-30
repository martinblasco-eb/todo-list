from django.conf.urls import url

from . import views

urlpatterns = [
    # url(r'create/$', views.TaskCreate.as_view(), name='task-create'),
    url(r'(?P<event_id>[0-9]+)/create/$', views.TaskCreate.as_view(), name='task-create'),
    url(r'(?P<event_id>[0-9]+)/update/(?P<pk>[0-9]+)/$', views.TaskUpdate.as_view(), name='task-update'),
    url(r'(?P<event_id>[0-9]+)/delete/(?P<pk>[0-9]+)/$', views.TaskDelete.as_view(), name='task-delete'),
    url(r'check/(?P<pk>[0-9]+)/$', views.check_task, name='task-check'),
    url(r'event', views.EventList.as_view(), name='event-list'),
    url(r'(?P<event_id>[0-9]+)/list/$', views.TaskList.as_view(), name='task-list'),
]
