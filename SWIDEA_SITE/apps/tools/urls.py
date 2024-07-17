from django.urls import path
from .views import *

app_name = 'tools'

urlpatterns = [
    path('', tool_list, name='list'),
    path('create/', tool_create, name='create'),
    path('<int:pk>/update/', tool_update, name='update'),
    path('<int:pk>/', tool_detail, name='detail'),
    path('<int:pk>/delete/', tool_delete, name='delete'),
]
