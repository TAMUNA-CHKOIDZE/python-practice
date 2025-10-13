from rest_framework import serializers
from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    # მომხმარებელს რომ გამოუჩნდეს category-იის ინტეჯერების მნიშვნელობები ტექსტურად
    category_display = serializers.CharField(source='get_category_display', read_only=True)
    # ფასს დაემატოს ევრო სიმბოლო
    price_with_currency = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'category', 'category_display', 'price', 'price_with_currency']

    def get_price_with_currency(self, obj):
        return f"{obj.price} €"
