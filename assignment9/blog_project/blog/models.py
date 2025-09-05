from django.db import models

class Post(models.Model):
    title = models.CharField(verbose_name='სათაური', max_length=100)
    content = models.TextField(verbose_name='ტექსტი', )
    created_at = models.DateTimeField(verbose_name='შექმნის დრო', auto_now_add=True)
    category = models.CharField(verbose_name='კატეგორია', max_length=100)