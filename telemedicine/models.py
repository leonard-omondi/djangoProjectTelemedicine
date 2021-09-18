from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):  # Each class will be its own table in the database
    name = models.CharField(max_length=100)
    doctor = models.TextField()
    date_last_visit = models.DateTimeField(default=timezone.now)
    current_medications = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name