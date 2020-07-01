from django.contrib import admin
from django.urls import path, include
from home.views import Index

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('', Index.as_view(), name='index'),
]