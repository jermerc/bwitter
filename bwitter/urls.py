from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from . import views

urlpatterns = [
    path('home/', PostListView.as_view(), name='bwitter-home'),
    path('about/', views.about, name='bwitter-about'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('', views.redirectHomepage),
    path('post/new_post', PostCreateView.as_view(), name='post-form'),
]

