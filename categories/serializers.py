from rest_framework import serializers
from categories.models import Category


class CategorySerializer(serializers.ModelSerializer):
    category = serializers.ReadOnlyField(source='category.category')

    class Meta:
        model = Category
        fields = ['id', 'category', 'created_at', 'updated_at']