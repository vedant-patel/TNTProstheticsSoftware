from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create_user/', views.create_user, name='create_user'),
    path('', views.index, name='index'),
]
