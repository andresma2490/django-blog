from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.db.models import Q

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import Article, Category
from .forms import ArticleForm
from .decorators import validate_author, validate_is_editor

class ArticleList(ListView):
    model = Article
    template_name = 'articles/home.html'
    context_object_name = 'articles'
    ordering = ['-id']
    paginate_by = 6
    
    def get_queryset(self):
        if self.request.GET.get('title'):
            return Article.objects.filter(Q(title__icontains=self.request.GET.get('title'))).order_by(*self.ordering)

        if self.request.GET.get('category'):
            search_category = get_object_or_404(Category, name=self.request.GET.get('category'))
            return Article.objects.filter(categories=search_category).order_by(*self.ordering)
        
        return super(ArticleList, self).get_queryset()

@method_decorator(login_required, name='dispatch')
@method_decorator(validate_is_editor, name='dispatch')
class ArticleCreate(CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'articles/article_form.html'
    
    def get_success_url(self):
        return reverse('articles:article_detail', kwargs={'slug': self.object.slug})

    def form_valid(self, form):
        form.instance.author = self.request.user

        if Article.objects.filter(author=form.instance.author, title=form.instance.title).first():
            form.add_error("title", "You have another article with the same title")
            return super(ArticleCreate, self).form_invalid(form)
            
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
        return reverse('articles:article_detail', kwargs={'slug': self.object.slug})

    def form_valid(self, form):
        article_exist = Article.objects.filter(author=self.request.user, title=form.instance.title).first()
        if article_exist and article_exist != self.get_object():
            form.add_error("title", "You have another article with the same title")
            return super(ArticleUpdate, self).form_invalid(form)
            
        return super(ArticleUpdate, self).form_valid(form)

@method_decorator(login_required, name='dispatch')
@method_decorator(validate_author, name='dispatch')
class ArticleDelete(DeleteView):
    model = Article
    template_name = 'articles/article_delete.html'
    
    def get_success_url(self):
        return reverse('articles:home')