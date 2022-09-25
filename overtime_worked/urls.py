from django.urls import path
from .views import *


app_name = 'overtime_worked'

urlpatterns = [
    path('list', OvertimeWorkedListView.as_view(), name='list_overtime_worked'),
    path('create-overtime_worked/', OvertimeWorkedCreateView.as_view(), name='create_overtime_worked'),
    path('edit-overtime_worked/<int:pk>', OvertimeWorkedEditView.as_view(), name='edit_overtime_worked'),
    path('delete-overtime_worked/<int:pk>', OvertimeWorkedDeleteView.as_view(), name='delete_overtime_worked'),
]
