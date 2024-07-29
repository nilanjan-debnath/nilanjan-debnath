from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from .models import Projects, Expriences
from django.template.defaulttags import register

@register.filter(name='split')
def split(value, separator):
    return value.split(separator)

def projects(request):
    projects = Projects.objects.all().order_by('index')
    return render(request, "projects.html", {"projects":projects})

def experiences(request):
    experiences = Expriences.objects.all().order_by('-enddate')
    return render(request, "experiences.html", {"experiences":experiences})

def about(request):
    return render(request, "about.html")