from django.contrib import admin
from django.urls import path
from .views import *


app_name = 'company'
urlpatterns = [
    path('create-company', CompanyCreateView.as_view(), name='create-company'),
    path('edit-company/<int:pk>', CompanyEditView.as_view(), name='edit-company'),
]
