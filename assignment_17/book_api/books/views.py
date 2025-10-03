from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from books.models import Book
from books.serializers import BookSerializer


@api_view(['GET'])
def books_list(request):
    books = Book.objects.filter(is_deleted=False)
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


class BookDetail(APIView):
    def get(self, request, id):
        book = Book.objects.filter(id=id, is_deleted=False).first()
        if book is None:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)
