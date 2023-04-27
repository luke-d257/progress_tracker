from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from .forms import LoginForm

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path("<int:pk>/", views.closer, name='closer'),
    path("<int:pk>/delete/", views.delete, name='delete'),
    path("<int:pk>/editProject/", views.editProject, name='editProject'),
    path('logout/', views.log_out, name="logout"),
    path('newProject/', views.newProject, name='newProject'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('myProjects/', views.myProjects, name='myProjects'),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.signup, name="signup"),
    path('login/', auth_views.LoginView.as_view(template_name = 'core/login.html',authentication_form = LoginForm), name='login')
]