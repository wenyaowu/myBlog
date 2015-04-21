from datetime import datetime
from django.db import models
from django.template.defaultfilters import slugify
from django_markdown.models import MarkdownField
# Create your models here.

class Tag(models.Model):
    slug = models.SlugField(max_length=200, unique=True)
    def __unicode__(self):
        return self.slug


class ArticleQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publish=True)

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
    text = MarkdownField()
    pub_datetime = models.DateTimeField(default=datetime.now, blank=True)
    mod_date_time = models.DateTimeField(auto_now=True)
    views = models.IntegerField(default=0)
    replies = models.IntegerField(default=0)
    publish = models.BooleanField(default=True)

    category = models.ForeignKey(Category, null=True)
    tags = models.ManyToManyField(Tag)

    objects = ArticleQuerySet.as_manager()

    def __unicode__(self):
        return self.title

    def save(self, *args, **kargs):
        self.slug = slugify(self.title)
        super(Article, self).save(*args, **kargs)

    class Meta:
        verbose_name = 'Blog Article'
        verbose_name_plural = 'Blog Articles'
        ordering = ["-pub_datetime"]