from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Task)
admin.site.register(Post)
admin.site.register(Classroom)
admin.site.register(Message)
