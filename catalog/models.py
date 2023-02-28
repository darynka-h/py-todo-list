from django.contrib.auth.models import AbstractUser
from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Executor(AbstractUser):
    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"


class Task(models.Model):
    content = models.CharField(max_length=255)
    time_creation = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(blank=True, null=True)
    done = models.BooleanField(default=False)
    task_tag = models.ManyToManyField(Tag)

    # class Meta:
    #     ordering = ["-time_creation", ]
