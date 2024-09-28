

from django.shortcuts import render
from rest_framework import mixins, viewsets
from rest_framework.response import Response
from .models import Blog, Category
from .serializers import BlogSerializer, CategorySerializer

# Create your views here.

class BlogApiView(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = 'slug'
    
class CategoryApiView(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'id'

class CategoryPostApiView(viewsets.ViewSet):
    def retrieve(self, request,pk=None):
        queryset = Blog.objects.filter(category=pk)
        serializer = BlogSerializer(queryset, many=True)
        return Response(serializer.data)

class PopularPostsApiView(viewsets.ViewSet):
    def list(self, request,pk=None):
        queryset = Blog.objects.filter(postlabel__iexact='POPULAR').order_by('-id')[0:4]
        serializer = BlogSerializer(queryset, many=True)
        return Response(serializer.data)
