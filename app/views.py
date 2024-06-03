from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods

def index(request):
    return render(request, "projects.html")