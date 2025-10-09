from django.contrib import admin

from articles.models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'published_date', ]
    search_fields = ['title', 'author']
    list_filter = ['published_date']

admin.site.register(Article, ArticleAdmin)
