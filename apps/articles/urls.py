from django.urls import path
from . import views

app_name = "articles"

urlpatterns = [
    path('', views.ArticleList.as_view(), name='home'),
    path('article/create/', views.ArticleCreate.as_view(), name='article_create'),
    path('article/<pk>/', views.ArticleDetail.as_view(), name='article_detail'),
    path('article/<pk>/edit/', views.ArticleUpdate.as_view(), name='article_edit'),
    path('article/<pk>/delete/', views.ArticleDelete.as_view(), name='article_delete')
]