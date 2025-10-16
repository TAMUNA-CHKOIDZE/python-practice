from django.db import models
from django.conf import settings  # ამის საშუალებით ავიღებთ AUTH_USER_MODEL-ს და არტიკლის author იქნება მომხმარებელი, რომელიც CustomUser-ით შეიქმნება და არ გამოვიყენებ ჯანგოს დეფაულტ user-ს


class Article(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='articles', verbose_name='author')
    title = models.CharField(max_length=255, verbose_name='title')
    content = models.TextField(verbose_name='content')
    published = models.BooleanField(default=False, verbose_name='published')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='created at')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='updated at')

    class Meta:
        verbose_name = 'article'
        verbose_name_plural = 'articles'

    def __str__(self):
        return self.title
