from rest_framework import serializers


class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=100)
    published_date = serializers.DateField()
    author = serializers.CharField(max_length=100)
