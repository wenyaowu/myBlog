from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from blog.models import Article, Category, Tag

# Create your views here.


def index(request):
    context_dict = {'header_image': 'home.jpg', 'header_title':'CODER SHACK'}
    articles = Article.objects.all()[:5]
    context_dict['articles'] = articles
    return render(request, 'blog/index.html', context_dict)


def about_me(request):
    context_dict = {'header_image': 'home.jpg', 'header_title':'ABOUT'}
    return render(request, 'blog/about_me.html', context_dict)


def category(request, category_name_slug):
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_name_slug)
        context_dict['category'] = category
        context_dict['category_name'] = category.name

        articles = Article.objects.filter(category=category)[:5]
        context_dict['articles'] = articles

        context_dict['header_image'] = category.name+'.jpg'
        context_dict['header_title'] = category.name.upper()

    except Category.DoesNotExist:
        pass

    return render(request, 'blog/category.html', context_dict)


def article(request, article_title_slug):
    context_dict = {}

    try:
        article = Article.objects.get(slug=article_title_slug)
        context_dict['article'] = article
        context_dict['header_image'] = article.category.name+'.jpg'
        context_dict['header_title'] = article.category.name
    except Article.DoesNotExist:
        pass

    return render(request, 'blog/article.html', context_dict)

def tag(request, tag_name_slug):
    context_dict = {}

    try:
        tag = Tag.objects.get(slug=tag_name_slug)
        context_dict['tag'] = tag

        articles = Article.objects.filter(tags=tag)
        context_dict['articles'] = articles
        context_dict['header_image'] = 'blog.jpg'
        context_dict['header_title'] = 'BLOG'
    except Tag.DoesNotExist:
        pass

    return render(request, 'blog/tag.html', context_dict)