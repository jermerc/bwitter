from django.shortcuts import render

posts = [
    {
        'author' : 'jermerc',
        'title' : 'Post 1',
        'content' : 'Blog Post 1!',
        'date_posted': 'June 6, 2020'
    },
    {
        'author': 'jermerc',
        'title' : 'Post 2',
        'content' : 'Blog Post 2!',
        'date_posted': 'June 6, 2020'
    }
]

# Create your views here.
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'bwitter/home.html', context)

def about(request):
    return render(request, 'bwitter/about.html', {'title': 'Bwitter About'})
