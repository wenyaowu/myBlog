from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from blog.models import Article, Category

# Create your views here.


def index(request):
    context_dict = {'header_image': 'home.jpg', 'title':'Coder Shack'}
    return render(request, 'blog/index.html', context_dict)


def about_me(request):
    context_dict = {'header_image': 'home.jpg', 'title':'About Me'}
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
        context_dict['title'] = category.name
    except Category.DoesNotExist:
        pass

    return render(request, 'blog/category.html', context_dict)

