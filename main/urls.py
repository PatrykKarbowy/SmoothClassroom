from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    
    
    path('sign_up', views.sign_up, name='sign_up'),
    path('change_password', views.change_password, name='change_password'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='reset_password'),
    path('password_reset_sent/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('password_reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    
    path('create_post', views.create_post, name='create_post'),
    path('create_task', views.create_task, name='create_task'),
    path('create_classroom', views.create_classroom, name='create_classroom'),
    path('classroom/<str:id>', views.classroom, name='classroom'),
    path('send_message', views.send_message, name='send_message'),
    path('classroom/get_messages/<str:id>', views.get_messages, name='get_messages'),
]