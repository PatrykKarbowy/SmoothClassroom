from django.forms import ModelForm, DateInput, ValidationError
from .models import Lesson

class AdminLessonForm(ModelForm):
    class Meta:
        model = Lesson
        widgets = {
            'start_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
            'end_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M')
        }
        fields = ['student','subject', 'description', 'start_time', 'end_time']
    
    def __init__(self, *args, **kwargs):
        super(AdminLessonForm, self).__init__(*args, **kwargs)
        self.fields['start_time'].input_formats=('%Y-%m-%dT%H:%M')
        self.fields['end_time'].input_formats=('%Y-%m-%dT%H:%M')
        
    def clean(self):
        cleaned_data = super().clean()
        start = cleaned_data['start_time']
        end = cleaned_data['end_time']

        queryset = Lesson.objects.exclude(pk=self.instance.pk).filter(
            start_time__lte=end, end_time__gte=start
        )

        if end <= start:
            raise ValidationError('End time cannot be lower than start time!')
        if queryset.exists():
            raise ValidationError('There is a lesson with this date range')
        return cleaned_data
        
class LessonForm(AdminLessonForm):
    def __init__(self, *args, **kwargs):
        super(AdminLessonForm, self).__init__(*args, **kwargs)
        del self.fields['student']