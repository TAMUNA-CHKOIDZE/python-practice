from django.urls import path

from books.views import books_list, BookDetail

urlpatterns = [
    path('', books_list, name='books_list'),
    path('<int:id>/', BookDetail.as_view(), name='book_detail')
]
