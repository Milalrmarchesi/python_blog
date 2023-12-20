from django.urls import path
from .views import post_list, add_post, search_posts, about, blog_list, blog_detail, add_blog, edit_blog, delete_blog, page_not_found

urlpatterns = [
    path('posts/', post_list, name='post_list'),
    path('add_post/', add_post, name='add_post'),
    path('search/', search_posts, name='search_posts'),
    path('about/', about, name='about'),
    path('pages/', blog_list, name='blog_list'),
    path('pages/<int:blog_id>/', blog_detail, name='blog_detail'),
    path('add_blog/', add_blog, name='add_blog'),
    path('edit_blog/<int:blog_id>/', edit_blog, name='edit_blog'),
    path('delete_blog/<int:blog_id>/', delete_blog, name='delete_blog'),
    path('<path:unknown_path>/', page_not_found, name='page_not_found'),
]
