from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Post

class HomePageView(TemplateView):
    template_name = 'home.html'

class PostsView(ListView):
    template_name = 'de.html'
    model = Post

class PostsDetailsView(DetailView):
    template_name = 'post_details.html'
    model = Post
