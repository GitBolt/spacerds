from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User

from blog.models import Blog

class BloglistView(ListView):
    model = Blog
    template_name = 'bloglist.html'
    context_object_name = 'blog'
    ordering = ['-date']


class BlogdetailView(DetailView):
    model = Blog
    template_name = 'blogdetail.html'










         

