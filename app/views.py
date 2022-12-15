from django.shortcuts import render, get_object_or_404
from .models import FM

def index(request):
    return render(request, 'app_temp/index.html', {})

def posts(request):
    posts = FM.objects.all()
    return render(request, 'app_temp/posts.html', {'posts': posts})

def article(request, id_slug):
    post = get_object_or_404(FM, slug=id_slug)
    return render(request, 'app_temp/article.html', {
            'post': post, 
            'id_slug': id_slug,
        })