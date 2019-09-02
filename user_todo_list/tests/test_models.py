import unittest
from django.test import TestCase
from django.contrib.auth.models import User
from ..models import Priority, Task
from datetime import datetime

# Create your tests here.
class TestModel(TestCase):

    def setUp(self):
        self.user=User.objects.create_user('bar2', password='foo')
        self.user.is_superuser=True
        self.user.is_staff=True
        self.user.save()

    def test_priority_name(self):
        priority = Priority.objects.create(name='normal')
        self.assertEqual(priority.name, 'normal')

    def test_task_user(self):
        date = datetime.now()
        priority = Priority.objects.create(name='low')
        event = '1234'
        task = Task.objects.create(name='buy', priority=priority, created=date, changed=date, user=self.user, event=event)
        self.assertEqual(task.user, self.user)

