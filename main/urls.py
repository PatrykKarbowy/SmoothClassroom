from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('sign_up', views.sign_up, name='sign_up'),
    path('create-post', views.create_post, name='create-post'),
    path('create_task', views.create_task, name='create_task'),
    path('create_classroom', views.create_classroom, name='create_classroom'),
    path('classroom/<str:id>', views.classroom, name='classroom'),
    path('send_message', views.send_message, name='send_message'),
]