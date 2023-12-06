from django.urls import path
from .views import post_list, add_post, search_posts

urlpatterns = [
    path('posts/', post_list, name='post_list'),
    path('add_post/', add_post, name='add_post'),
    path('search/', search_posts, name='search_posts'),
]
