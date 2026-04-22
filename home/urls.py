from django.urls import path
from home import views


urlpatterns = [
    path('', views.list_create_view, name='home')
]