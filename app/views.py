from django.shortcuts import render, get_object_or_404
from .models import FM, Vacancy

def index(request):
    return render(request, 'app_temp/index.html', {})

def posts(request):
    posts = FM.objects.all()
    vacancies = Vacancy.objects.all()
    return render(request, 'app_temp/posts.html', {
        'posts': posts, 
        'vacancies': vacancies,
    })

def vacancies(request, id_slug_vac):
    vac = get_object_or_404(Vacancy, slug_vac=id_slug_vac)
    return render(request, 'app_temp/vacancy.html', {
        'vac': vac,
        'id_slug_vac': id_slug_vac,
    })


def article(request, id_slug):
    post = get_object_or_404(FM, slug=id_slug)
    return render(request, 'app_temp/article.html', {
            'post': post, 
            'id_slug': id_slug,
        })