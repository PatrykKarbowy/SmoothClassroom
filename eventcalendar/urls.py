from django.urls import path
from . import views

urlpatterns = [
    path('', views.CalendarView.as_view(), name='calendar'),
    path('add_lesson', views.LessonCreateView.as_view(), name='add_lesson'),
    path('edit_lesson/<str:pk>', views.LessonUpdateView.as_view(), name='edit_lesson'),
    path('delete_lesson/<str:pk>', views.LessonDeleteView.as_view(), name='delete_lesson'),
    path('accept_lesson/<str:pk>', views.LessonAcceptView.as_view(), name='accept_lesson'),
]