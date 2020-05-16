from django.shortcuts import render
from .models import Project

def home(request):
    egg = Project.objects.all()
    return render(request, 'portfolio/home.html', {'bon':egg})
