from django.db import models
from django.contrib.auth.models import User
from main.models import Classroom
from django.core.mail import send_mail
from website.settings import DEFAULT_FROM_EMAIL


class Lesson(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    description = models.CharField(max_length = 200)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    accepted = models.BooleanField(default=False)
    
    def save(self, *args, **kwargs):
        if self.accepted == True:
            title = f'{self.student.username} Lekcja zaakcpetowana - {self.start_time}'
            body = f'Twoja lekcja została zaakceptowana, widzimy się na Skype dnia {self.start_time}'
            send_mail(title, 
                      body, 
                      from_email=DEFAULT_FROM_EMAIL,
                      recipient_list=[self.student.email],
                      fail_silently=False
                      )
        return super().save(*args, **kwargs)