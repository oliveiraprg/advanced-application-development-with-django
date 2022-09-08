from django.contrib import admin
from django.urls import path
from .views import *


app_name = 'company'
urlpatterns = [
    path('create-company', CompanyCreateView.as_view(), name='create_company'),
]
