from django.urls import path
from .views import *


app_name = 'documents'

urlpatterns = [
    path('list', DocumentListView.as_view(), name='list_documents'),
    path('create-document/<int:collaborator_id>/', DocumentCreateView.as_view(), name='create_document'),
    path('edit-document/<int:pk>', DocumentEditView.as_view(), name='edit_document'),
    path('delete-document/<int:pk>', DocumentDeleteView.as_view(), name='delete_document'),
]
