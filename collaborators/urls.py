from django.contrib import admin
from django.urls import path
from .views import *


app_name = 'collaborators'

urlpatterns = [
    path('', CollaboratorsListView.as_view(), name='list_collaborators'),
    path('create-collaborator/', CollaboratorCreateView.as_view(), name='create_collaborators'),
    path('edit-collaborator/<int:pk>', CollaboratorEditView.as_view(), name='edit_collaborators'),
    path('delete-collaborator/<int:pk>', CollaboratorDeleteView.as_view(), name='delete_collaborators'),
]
