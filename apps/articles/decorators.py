from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect

from .models import Article

def validate_author(function):
    def wrap(request, *args, **kwargs):
        article = get_object_or_404(Article, pk=kwargs.get("pk"))
        
        if not request.user == article.author:
            return redirect(reverse_lazy("articles:home"))

        return function(request, *args, **kwargs)

    return wrap

def validate_is_editor(function):
    def wrap(request, *args, **kwargs):
        if not request.user.is_editor:
            return redirect(reverse_lazy("articles:home"))

        return function(request, *args, **kwargs)

    return wrap