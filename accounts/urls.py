from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name = 'accounts/login.html') , name='login'),
    path('profile/', views.profile,name='profile'),
    path('logout/', views.logout_user, name='logout'),

]
