from django.db import models
from django.conf import settings


class Priority(models.Model):
    name = models.CharField(max_length=120)
    
    def __str__(self):
        return self.name


class Task(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=120)
    priority = models.ForeignKey(Priority, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    changed = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
      settings.AUTH_USER_MODEL,
      on_delete=models.CASCADE,
      default=None
    )
    done = models.BooleanField(default=False)

