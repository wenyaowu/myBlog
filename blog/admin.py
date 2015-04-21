from django.contrib import admin
from models import Category, Article, Tag
from django_markdown.admin import MarkdownModelAdmin
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class ArticleAdmin(MarkdownModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Tag)