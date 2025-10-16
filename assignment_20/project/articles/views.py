from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from articles.models import Article
from articles.permissions import IsAuthor
from articles.serializers import ArticleListSerializer, ArticleDetailSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return ArticleListSerializer
        return ArticleDetailSerializer

    # perform_create საშუალებს გვაძლევს, რომ ავტორიზებული მომხმარებელი რომელიც შემოსულია და ქმნის article ობიეტქს ავტომატურად გახდეს სტატიის ავტორი
    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy', 'publish']:
            permission_classes = [IsAuthenticated, IsAuthor]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(detail=True, methods=['post'])
    def publish(self, request, pk=None):
        article = self.get_object()
        article.published = True
        article.save(update_fields=['published'])
        return Response({'status': 'published'}, status=status.HTTP_200_OK)
