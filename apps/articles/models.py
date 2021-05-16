from django.db import models
from apps.users.models import User

class Category(models.Model):
    name = models.CharField(primary_key=True, max_length=50)
    
    class Meta:
        verbose_name_plural = "categories"
    
    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(default='articles/article_default_image.jpg', upload_to="articles")
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    author = models.ForeignKey(User, null=False, blank=False, on_delete=models.PROTECT)
    categories = models.ManyToManyField(Category)

    class Meta:
        ordering = ['-date_created']
    
    def __str__(self):
        return self.title