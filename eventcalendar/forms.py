from sqlite3 import Date
from django.forms import ModelForm, DateInput
from .models import Lesson

class LessonForm(ModelForm):
    class Meta:
        model = Lesson
        widgets = {
            'start_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
            'end_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M')
        }
        fields = ['subject', 'description', 'start_time', 'end_time']
    
    def __init__(self, *args, **kwargs):
        super(LessonForm, self).__init__(*args, **kwargs)
        self.fields['start_time'].input_formats=('%Y-%m-%dT%H:%M')
        self.fields['end_time'].input_formats=('%Y-%m-%dT%H:%M')