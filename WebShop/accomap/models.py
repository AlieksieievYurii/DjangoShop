from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify


# Utils for models
def _image_folder(instance, file_name):
    file_name = '{slug}.{format}'.format(slug=instance.slug, format=file_name.split('.')[1])
    return '{}/{}'.format(instance.slug, file_name)


def _pre_save_category_slug(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.name)


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(blank=True)

    def __str__(self):
        return self.name


pre_save.connect(_pre_save_category_slug, sender=Category)


class Brand(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    slug = models.SlugField()
    description = models.TextField()
    image = models.ImageField(upload_to=_image_folder)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.title
