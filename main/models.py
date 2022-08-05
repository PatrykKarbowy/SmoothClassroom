from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return self.title + '\n' + self.description
    
class Task(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    finished = models.BooleanField(default = False)
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return self.title
    
class Classroom(models.Model):
    students = models.ManyToManyField(User)
    name = models.CharField(max_length = 200)
    
    def __str__(self):
        return self.name