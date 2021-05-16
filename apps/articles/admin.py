from django.contrib import admin
from .models import Article, Category

class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ('date_created', 'date_updated')
    list_display = ('title', 'author', 'date_created')
    ordering = ('-date_created', )
    search_fields = ('title', 'content', 'author__username', 'categories__name')

admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)
