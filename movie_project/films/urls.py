from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # URL-паттерн для главной страницы
    path('show/', views.show, name='show'),  # Другие паттерны
    path('create/', views.create, name='create'),
]

