from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name='title')
    content = models.TextField(verbose_name='content')
    author = models.CharField(max_length=100, verbose_name='author')
    published_date = models.DateTimeField(auto_now_add=True, verbose_name='publish date')
    article_deleted = models.BooleanField(default=False, verbose_name='article deleted')

    class Meta:
        verbose_name = 'article'
        verbose_name_plural = 'articles'

    def __str__(self):
        return self.title


