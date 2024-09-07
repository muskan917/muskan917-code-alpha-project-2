from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post-list'),
    path('like/<int:post_id>/', views.like_post, name='like-post'),
    path('comment/<int:post_id>/', views.add_comment, name='add-comment'),
]
