from rest_framework import serializers
from categories.models import Category


class CategorySerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='category', read_only=True)

    class Meta:
        model = Category
        fields = ['name', 'created_at', 'updated_at']