from django.shortcuts import render
from .models import all_blog

def test(request):
    egg = all_blog.objects.all()
    return render(request, 'blog/all_blogs.html', {'bon':egg})
