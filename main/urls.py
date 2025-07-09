from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
   
    path('', views.home, name='home'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('quizzes/', views.quiz_list, name='quiz_list'),
    path('quiz/<int:topic_id>/', views.quiz_questions, name='quiz_questions'),
    path('dashboard/', views.dashboard, name='dashboard'),
     path('add-question/', views.add_question, name='add_question'),
     path('password_reset/', auth_views.PasswordResetView.as_view(template_name='main/password_reset.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='main/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='main/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='main/password_reset_complete.html'), name='password_reset_complete'),
    path('resources/', views.interview_resources, name='interview_resources'),
     path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
]