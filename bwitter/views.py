from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

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

class PostListView(ListView):
    model = Post
    template_name = 'bwitter/home.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted'] # Sorts posts newest to oldest.

class PostDetailView(DetailView):
    model = Post
    template_name = 'bwitter/post_detail.html'

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    template_name = 'bwitter/post_form.html'
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'bwitter/post_form.html'
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False