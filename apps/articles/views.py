from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.db.models import Q

from .models import Article, Category
from .forms import ArticleForm

class ArticleList(ListView):
    model = Article
    template_name = 'articles/home.html'
    
    def get_queryset(self):
        if self.request.GET.get('title'):
            return Article.objects.filter(Q(title__icontains=self.request.GET.get('title')))

        if self.request.GET.get('category'):
            search_category = get_object_or_404(Category, name=self.request.GET.get('category'))
            return Article.objects.filter(categories=search_category)
        
        return super(ArticleList, self).get_queryset()

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