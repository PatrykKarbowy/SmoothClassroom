from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    
    path('sign_up', views.sign_up, name='sign_up'),
    path('password_change/', auth_views.PasswordChangeView.as_view(
        template_name='registration/password_change.html',
        ), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='registration/password_change_complete.html'
        ), name='password_change_done'),
    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='registration/password_reset.html'
        ), name='reset_password'),
    path('password_reset_sent/', auth_views.PasswordResetDoneView.as_view(
        template_name='registration/password_reset_success.html'
        ), name="password_reset_done"),
    path('password_reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(
        template_name='registration/password_reset_confirmation.html'
        ), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='registration/password_reset_completed.html'
        ), name='password_reset_complete'),
    
    path('create_post', views.create_post, name='create_post'),
    path('update_post/<str:id>', views.update_post, name='update_post'),
    path('search_post/', views.SearchResultsListView.as_view(), name='search_post_results'),
    path('create_task', views.create_task, name='create_task'),
    path('create_classroom', views.create_classroom, name='create_classroom'),
    path('classroom/<str:id>', views.classroom, name='classroom'),
    path('send_message', views.send_message, name='send_message'),
    path('classroom/get_messages/<str:id>', views.get_messages, name='get_messages'),
]