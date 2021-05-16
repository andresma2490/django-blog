from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse

from .models import Article
from .forms import ArticleForm

class ArticleList(ListView):
    model = Article
    template_name = 'articles/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articles'] = Article.objects.all()
        return context


class ArticleCategory(ListView):
    model = Article
    template_name = 'articles/home.html'

    def get_queryset(self):
        category = get_object_or_404(Category, name=self.kwargs['category_id'])
        return Article.objects.filter(categories=category)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articles'] = self.get_queryset()
        return context


class ArticleCreate(CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'articles/article_form.html'
    
    def get_success_url(self):
        return reverse('articles:article_detail', kwargs={'pk': self.object.pk})


class ArticleDetail(DetailView):
    model = Article
    template_name = 'articles/article_detail.html'


class ArticleUpdate(UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = 'articles/article_form.html'
    
    def get_success_url(self):
        return reverse('articles:article_detail', kwargs={'pk': self.object.pk})


class ArticleDelete(DeleteView):
    model = Article
    template_name = 'articles/article_delete.html'
    
    def get_success_url(self):
        return reverse('articles:home')