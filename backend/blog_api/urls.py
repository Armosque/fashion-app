
from django.urls import path, include
from .views import BlogApiView, CategoryApiView, CategoryPostApiView, PopularPostsApiView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('blogs', BlogApiView, basename='blogs')
router.register('category', CategoryApiView, basename='category')
router.register('categoryBlogs', CategoryPostApiView, basename='categoryBlogs')
router.register('populares', PopularPostsApiView, basename='populares')

urlpatterns = [
    path('', include(router.urls)),
    
]