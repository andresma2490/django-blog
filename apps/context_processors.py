from apps.articles.models import Article, Category
from django.conf import settings

from apps.users.models import User


def debug(request):
  return {'DEBUG': settings.DEBUG}

def getCategories(request):
    return {'categories': Category.objects.all()}

def getPopularArticles(request):
    return {'popular_articles': Article.objects.all().order_by('id')[:3]}

def about(request):
    return {'about': User.objects.get(id=1).description}
