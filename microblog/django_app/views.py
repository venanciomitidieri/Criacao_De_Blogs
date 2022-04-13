from django.shortcuts import render, render_to_response, get_object_or_404
from django_app.models import Blog, Categoria
from django.http import HttpResponse


def index(request):
    return render_to_response('django\home.html', {
        'categorias': Categoria.objects.all(),
        'posts': Blog.objects.all()[:5]
    })


def ver_post(request, slug):
    return render_to_response('django\\ver_post.html', {
        'post': get_object_or_404(Blog, url=slug)
    })


def ver_categoria(request, slug):
    categoria = get_object_or_404(Categoria, url=slug)
    return render_to_response('django\\ver_categoria.html', {
        'categoria': categoria,
        'posts': Blog.objects.filter(categoria=categoria)[:5]
    })