from django.urls import include, path
from rest_framework.routers import DefaultRouter

from articles.views import ArticlesViewSet

router = DefaultRouter()
router.register(r'', ArticlesViewSet, basename='articles')

urlpatterns = [
    path('', include(router.urls)),
]
