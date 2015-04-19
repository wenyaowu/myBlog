from datetime import datetime
from django.db import models
from django.template.defaultfilters import slugify
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    slug = models.SlugField(unique=True, default='')
    def __unicode__(self):
        return self.name
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)


class Article(models.Model):
    title = models.CharField(max_length=128, unique=True)
    slug = models.SlugField(unique=True, default='')
    text = models.TextField(blank=True)
    pub_datetime = models.DateTimeField(default=datetime.now, blank=True)
    category = models.ForeignKey(Category, null=True)
    views = models.IntegerField(default=0)
    replies = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kargs):
        self.slug = slugify(self.title)
        super(Article, self).save(*args, **kargs)