from django.urls import path
from . import views

urlpatterns = [
    path('', views.random_wisdom),
    path('wisdom/<int:wisdom_id>/', views.wisdom_by_id)
]
