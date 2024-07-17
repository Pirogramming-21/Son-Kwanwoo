from django.urls import path
from .views import *

app_name = "posts"

urlpatterns = [
    path('', main, name='main'),
    path('create/', post_create, name='create'),
    path('<int:pk>/', post_detail, name='detail'),
    path('<int:pk>/update/', post_update, name='update'),
    path('<int:pk>/delete/', post_delete, name='delete'),
    path('update_interest/', update_interest, name='update_interest'),
    path('update_idea_star/', update_idea_star, name='update_idea_star'),
    
]