from django.urls import path

from books.views import books_list

urlpatterns = [
    path('books_list/', books_list, name='books_list'),
]
