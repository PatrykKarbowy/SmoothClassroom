from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('calendar/', include('eventcalendar.urls')),
    path('', include('django.contrib.auth.urls')),
]
