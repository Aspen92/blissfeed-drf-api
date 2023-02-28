from django.shortcuts import render
from rest_framework import generics, permissions
from categories.models import Category
from categories.serializers import CategorySerializer


class CategoriesDetail(generics.RetrieveAPIView):
    """
    Categories detailed view.
    """
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CategoriesList(generics.ListCreateAPIView):
    """
    Categories list view.
    """
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Category.objects.all()
