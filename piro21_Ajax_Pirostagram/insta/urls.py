from django.urls import path
from . import views

app_name = 'insta'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('like_ajax/', views.like_ajax, name='like_ajax'),
    path('comment_ajax/', views.comment_ajax, name='comment_ajax'),
    path('delete_comment_ajax/', views.delete_comment_ajax, name='delete_comment_ajax'),
]