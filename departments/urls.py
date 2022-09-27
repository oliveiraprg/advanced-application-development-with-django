from django.urls import path
from .views import *


app_name = 'departments'

urlpatterns = [
    path('list', DepartmentListView.as_view(), name='list_departments'),
    path('create-department/', DepartmentCreateView.as_view(), name='create_department'),
    path('edit-department/<int:pk>', DepartmentUpdateView.as_view(), name='edit_department'),
    path('delete-department/<int:pk>', DepartmentDeleteView.as_view(), name='delete_department'),
]
