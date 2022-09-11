from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.db.models import F
from .models import *

class Home(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 24

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Toofab'
        return context

class PostsByCategory(ListView):
    template_name = 'blog/category.html'
    context_object_name = 'posts'
    paginate_by = 24
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(slug=self.kwargs['slug'])
        context['thiscategory'] = self.kwargs['slug']
        return context

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs['slug'])

class PostsByTag(ListView):
    template_name = 'blog/category.html'
    context_object_name = 'posts'
    paginate_by = 24
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Posts by: ' + str(Tag.objects.get(slug=self.kwargs['slug']))
        return context

    def get_queryset(self):
        return Post.objects.filter(tags__slug=self.kwargs['slug'])


class GetPost(DetailView):
    model = Post
    template_name = 'blog/post.html'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        category = self.object.category.slug
        self.object.views = F('views') + 1
        self.object.save()
        self.object.refresh_from_db()
        context['posts'] = Post.objects.filter(category__slug=category).exclude(pk = self.object.id)[0:6]
        context['category'] = Post.objects.filter(category__slug=self.kwargs['slug'])
        return context

class Search(ListView):
    template_name = 'blog/search.html'
    context_object_name = 'posts'
    paginate_by = 24

    def get_queryset(self):
        return Post.objects.filter(title__icontains=self.request.GET.get('s'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['s'] = f"s={self.request.GET.get('s')}&"
        context['ss'] = f"{self.request.GET.get('s')}"
        return context