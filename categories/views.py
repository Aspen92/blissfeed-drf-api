from django.shortcuts import render
from rest_framework import generics, permissions
from categories.models import Category
from categories.serializers import CategorySerializer


class CategoriesDetail(generics.RetrieveAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CategoriesList(generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Category.objects.all()
