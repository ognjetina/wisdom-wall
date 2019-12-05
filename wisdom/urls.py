from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('', views.random_wisdom),
    path('admin/', admin.site.urls),
    path('wisdom/<int:wisdom_id>/', views.wisdom_by_id),
    path('wisdom/new/', views.post_new_wisdom, name='post_new_wisdom'),
    path('wisdoms/', views.wisdoms, name='wisdoms'),
    path('toxicity/', views.toxicity, name='toxicity'),
]
