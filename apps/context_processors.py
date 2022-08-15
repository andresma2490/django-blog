from apps.articles.models import Category
from django.conf import settings


def debug(request):
  return {'DEBUG': settings.DEBUG}

def getCategories(request):
    return {'categories': Category.objects.all()}