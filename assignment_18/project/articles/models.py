from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name='title')
    content = models.TextField(verbose_name='content')
    author = models.CharField(max_length=100, verbose_name='author')
    published_date = models.DateTimeField(auto_now_add=True, verbose_name='publish date')
