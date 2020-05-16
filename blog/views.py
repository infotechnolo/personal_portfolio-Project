from django.shortcuts import render, get_object_or_404
from .models import all_blog

def test(request):
    egg = all_blog.objects.order_by('-date')
    return render(request, 'blog/all_blogs.html', {'bon':egg})

def detail(request, blog_id):
    jon = get_object_or_404(all_blog, pk=blog_id)
    return render(request, 'blog/detail.html',{'bobby':jon})
