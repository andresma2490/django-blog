from django.db.models.signals import post_save
from django.dispatch import receiver

from PIL import Image

from .models import Article


@receiver(post_save, sender=Article)
def optimize_image(sender, instance, **kwargs):
    if instance.image:
        image = Image.open(instance.image.path)
        image.save(instance.image.path, quality=50, optimize=True)
