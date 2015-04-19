from django.test import TestCase
from django.utils import timezone
from blog.models import Article
# Create your tests here.

class test_creat_article(TestCase):
    def test_create_article(self):
        #Create the post
        article = Article()

        #Set attributes
        article.title = 'Test post'
        article.text = 'This the the blog post test'
        article.pub_datetime = timezone.now()

        #Save the article
        article.save()

        articles = Article.objects.all()
        self.assertEquals(len(articles), 1)
        only_article = articles[0]
        self.assertEqual(only_article, article)
