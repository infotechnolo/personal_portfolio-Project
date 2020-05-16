from django.shortcuts import render
from .models import all_blog

def all_blogs(request):
    all_blogs = all_blog.objects.all()
    return render(request, 'blog/all_blogs.html', {'all_blogs':all_blogs})
