"""Define URL patterns for blogs."""
from django.urls import path

from .import views

app_name = 'blogs'
urlpatterns = [
    # Home page; show all post in chronological order.
    path('', views.index, name='index'),
    # Page for adding new blog posts.
    path('new_post/', views.new_post, name='new_post'),
    # Page for editing a blog post.
    path('edit_post/', views.edit_post, name='edit_post'),
] 