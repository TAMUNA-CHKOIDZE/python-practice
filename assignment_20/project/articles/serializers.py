from django.conf import settings

from rest_framework import serializers
from articles.models import Article


# Author-სთვის ცალკე სერიალიზატორი, რომ მეტი ინფორმაცია აჩვენოს
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = settings.AUTH_USER_MODEL  # CustomUser
        fields = ['id', 'full_name', 'email']


# Article-ის სერიალიზატორი list ოპერაციისთვის
class ArticleListSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)  # Nested author info

    class Meta:
        model = Article
        fields = ['id', 'title', 'author']  # მოკლე ინფო ლისტისთვის
        read_only_fields = ['author', 'published', 'created_at', 'updated_at']


# Article-ის სერიალიზატორი detail, update, delete ოპერაციებისათვის
class ArticleDetailSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)  # Nested author info

    class Meta:
        model = Article
        fields = ['id', 'title', 'author', 'content', 'published', 'created_at', 'updated_at']
        read_only_fields = ['author', 'published', 'created_at', 'updated_at']
