from django.urls import path
from . import views

urlpatterns = [
    path('', views.projects, name="project"),
    path('experience', views.experiences, name="experience"),
    path('about', views.about, name="about"),
]
