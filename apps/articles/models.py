from django.db import models
from django.utils.text import slugify

from apps.users.models import User
from .utils import RichTextUploadingField

class Category(models.Model):
    name = models.CharField(primary_key=True, max_length=50)
    
    class Meta:
        verbose_name_plural = "categories"
    
    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    resume = models.TextField(null=False, blank=False)
    content = RichTextUploadingField()
    image = models.ImageField(default='default/article.jpg', upload_to="articles")
    keywords = models.TextField(null=True, blank=True)
    slug = models.SlugField(null=False, blank=False, unique=True)
    is_public = models.BooleanField(default=True)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    author = models.ForeignKey(User, null=False, blank=False, on_delete=models.PROTECT)
    categories = models.ManyToManyField(Category)

    class Meta:
        ordering = ['-date_created']
    
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        slug = "{title} by {author}".format(title=self.title, author=self.author.username)
        self.slug = slugify(slug)

        super(Article, self).save(*args, **kwargs)
        return self

class Favorites(models.Model):
    article_id = models.ForeignKey(Article, null=False, blank=False, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)