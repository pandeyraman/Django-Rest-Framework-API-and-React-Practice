from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'productName',
            'description',
        )
        model = Product