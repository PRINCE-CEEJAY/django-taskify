from django.urls import path
from home import views


urlpatterns = [
    path('', views.task_list_view, name='task_list'),
    path('create/', views.task_create_view, name='task_create'),
    path('update/<int:id>/', views.task_update, name='task_update'),
    path('delete/<int:id>/', views.tasK_delete, name='task_delete'),
]