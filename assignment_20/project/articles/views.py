from rest_framework import viewsets
from articles.models import Article
from articles.serializers import ArticleListSerializer, ArticleDetailSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return ArticleListSerializer
        return ArticleDetailSerializer



