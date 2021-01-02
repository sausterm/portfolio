from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('projects/', views.projects, name="projects"),
    path('project/', views.project, name="project"),
    path('profile/', views.profile, name="profile"),

]  