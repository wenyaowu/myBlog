from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from blog.models import Article, Category

# Create your views here.


def index(request):
    context_dict = {'header_image': 'home.jpg', 'header_title':'Coder Shack'}
    articles = Article.objects.all()[:5]
    context_dict['articles'] =articles
    return render(request, 'blog/index.html', context_dict)


def about_me(request):
    context_dict = {'header_image': 'home.jpg', 'header_title':'About Me'}
    return render(request, 'blog/about_me.html', context_dict)


def category(request, category_name_slug):
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_name_slug)
        context_dict['category'] = category
        context_dict['category_name'] = category.name

        articles = Article.objects.filter(category=category)
        context_dict['articles'] = articles

        context_dict['header_image'] = category.name+'.jpg'
        context_dict['header_title'] = category.name
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