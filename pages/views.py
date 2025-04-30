from django.shortcuts import render, get_object_or_404
from .models import Page
from products.models import Product
from blog.models import Post

# Create your views here.

def home(request):
    products = Product.objects.filter(is_active=True)
    posts = Post.objects.filter(status='published')[:3]
    return render(request, 'pages/home.html', {
        'products': products,
        'posts': posts
    })

def about(request):
    return render(request, 'pages/about.html')

def page_detail(request, slug):
    page = get_object_or_404(Page, slug=slug, is_published=True)
    return render(request, 'pages/page_detail.html', {'page': page})
