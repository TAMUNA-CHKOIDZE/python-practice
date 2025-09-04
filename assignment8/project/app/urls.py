from django.urls import path

from app.views import home, NotFound

urlpatterns = [
    path('home/', home, name='home'),
    path('not-found/', NotFound.as_view(), name='not_found'),
]