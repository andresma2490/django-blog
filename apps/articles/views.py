from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.db.models import Q

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import Article, Category
from .forms import ArticleForm
from .decorators import validate_author

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


@method_decorator(login_required, name='dispatch')
class ArticleCreate(CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'articles/article_form.html'
    
    def get_success_url(self):
        return reverse('articles:article_detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(ArticleCreate, self).form_valid(form)

class ArticleDetail(DetailView):
    model = Article
    template_name = 'articles/article_detail.html'


@method_decorator(login_required, name='dispatch')
@method_decorator(validate_author, name='dispatch')
class ArticleUpdate(UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = 'articles/article_form.html'
    
    def get_success_url(self):
        return reverse('articles:article_detail', kwargs={'pk': self.object.pk})


@method_decorator(login_required, name='dispatch')
@method_decorator(validate_author, name='dispatch')
class ArticleDelete(DeleteView):
    model = Article
    template_name = 'articles/article_delete.html'
    
    def get_success_url(self):
        return reverse('articles:home')