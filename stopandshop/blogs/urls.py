from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('my_blogs', myBlog, name='my_blog'),
    path('create_blog', createBlog, name='create_blog'),
    path('get_blogs/<str:pk>', getBlog, name='get_blog'),
    path('', blogs, name='blog'),
    path('update_blog/<int:pk>/', updateBlog, name='update_blog'),
    path('delete_blog/<int:pk>/', deleteBlog, name='delete_blog'),
    path('get_blog_video/<str:pk>', getBlogVideos, name='get_blog_video'),
    path('create_blog_video/', createBlogVideos, name='create_blog_video'),
    path('update_blog_video/<int:pk>/', updateBlogVideo, name='update_blog_video'),
    path('delete_blog_video/<int:pk>/', deleteBlogVideo, name='delete_blog_video'),
]