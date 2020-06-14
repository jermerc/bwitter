from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

# Create your views here.

# Homepage View containing a list of all the posts.
def home(request):
    context = {
        'posts': Post.objects.all(),
        'title': 'Bwitter Home'
    }
    response = render(request, 'bwitter/home.html', context)
    return response

# Simple about page.
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
    paginate_by = 5 # Shows only 2 pages per page. Paginate by 2 posts.

class UserPostListView(ListView):
    model = Post
    template_name = 'bwitter/user_posts.html'
    context_object_name = 'posts'
    order = ['-date_posted']
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

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

