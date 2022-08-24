from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Task, Classroom

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "description"]
        
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title"]
        
class ClassroomForm(forms.ModelForm):
    class Meta:
        model = Classroom
        fields = ["name", "students"]
    
    students = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        widget = forms.CheckboxSelectMultiple
    )