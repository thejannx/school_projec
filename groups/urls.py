from django.urls import path
from . import views

app_name = 'groups'

urlpatterns = [
    path('list/', views.group_list, name='list'),
    path('create/', views.group_create, name='create'),
    path('detail/<int:pk>/', views.group_detail, name='detail'),
]
