__author__ = 'evanwu'
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myBlog.settings')

import django
django.setup()

from blog.models import Category, Article

def populates():
    surf = add_cat('Surfing')
    add_article(cat=surf, title='Surfing101', text='This is Surfing101')
    add_article(cat=surf, title='Choosing a right board', text='This tell you how to chose right board')

    coding = add_cat('Coding')
    add_article(cat=coding, title='Pros and Cons', text='Pros and Cons for each languages')

def add_article(cat, title, text):
    a = Article.objects.get_or_create(category=cat, title=title, text=text)
    return a


def add_cat(name):
    c = Category.objects.get_or_create(name=name)[0]
    return c


if __name__ == '__main__':
    print "Starting Populating with dumpData"
    populates()