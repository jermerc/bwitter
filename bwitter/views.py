from django.shortcuts import render, redirect
from .models import Post

# Create your views here.
def home(request):
    context = {
        'posts': Post.objects.all(),
        'title': 'Bwitter Home'
    }
    response = render(request, 'bwitter/home.html', context)
    return response

def about(request):
    response = render(request, 'bwitter/about.html', {'title': 'Bwitter About'})
    return response

def redirectHomepage(request):
    response = redirect('/home/')
    return response
