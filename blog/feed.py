__author__ = 'evanwu'
from django.contrib.syndication.views import Feed
from blog.models import Article

class LatestPosts(Feed):
    title = "Code Shack"
    link = "/feed/"
    description = "Latest Posts"

    def items(self):
        return Article.objects.published()[:5]