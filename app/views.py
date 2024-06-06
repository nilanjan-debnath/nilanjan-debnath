from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods

def projects(request):
    return render(request, "projects.html")

def experiences(request):
    return render(request, "experiences.html")

def about(request):
    return render(request, "about.html")