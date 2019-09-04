import unittest
from unittest.mock import patch
from django.contrib.auth.models import User
from django.test import TestCase, Client
from eventbrite import Eventbrite
from ..models import Priority, Task
from social_django.models import UserSocialAuth
from datetime import datetime


# Create your tests here.
class TestView(TestCase):

    def setUp(self):
        self.user=User.objects.create_user(username='testuser', password='foo')
        UserSocialAuth.objects.create(
            user=self.user,
            provider='eventbrite',
            uid='34563456',
            extra_data={
                'auth_time': 1567447106, 
                'access_token': 'KLHJLJHLKJH', 
                'token_type': 'bearer',
            }
        )

    def test_user_logged_in(self):
        client = Client()
        response = client.post('/accounts/login/', {'username': 'testuser', 'password':'foo'})
        self.assertEqual(response.status_code, 302)

    def test_user_fail_logged_in(self):
        client = Client()
        response = client.post('/accounts/login/', {'username': 'testuser2', 'password':'foo'})
        self.assertEqual(response.status_code, 200)

    def test_task_create(self):
        priority = Priority.objects.create(name='low')
        date = datetime.now()
        url = '/task/{}/create'.format('23221')
        data =  {'name': 'task', 'priority':priority}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 301)
 
    def test_task_update(self):
        priority = Priority.objects.create(name='low')
        date = datetime.now()
        url = '/task/{}/update/{}'.format('23221','10')
        data =  {'name': 'task', 'priority':priority}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 301)

    def test_task_delete(self):
        priority = Priority.objects.create(name='low')
        date = datetime.now()
        url = '/task/{}/delete/{}'.format('23221','10')
        data =  {'name': 'task', 'priority':priority}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 301)

    def test_check_task(self):
        url = '/task/{}/check/{}'.format('23221','10')
        data =  {'name': 'task'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 301)

    def test_empty_get(self):
        eventbrite = Eventbrite(UserSocialAuth.objects.get(pk=1))
        response = eventbrite.get('/user/events/me')
        self.assertEqual(response.status_code, 404)

    def test_event_list(self):
        pass
