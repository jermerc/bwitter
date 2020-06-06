from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='bwitter-home'),
    path('about/', views.about, name='bwitter-about'),
]