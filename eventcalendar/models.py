from django.db import models
from django.contrib.auth.models import User
from main.models import Classroom

class Lesson(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    description = models.CharField(max_length = 200)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    accepted = models.BooleanField(default=False)
    