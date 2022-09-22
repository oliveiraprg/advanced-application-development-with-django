from django.urls import path
from .views import *


app_name = 'collaborators'

urlpatterns = [
    path('', CollaboratorListView.as_view(), name='list_collaborators'),
    path('create-collaborator/', CollaboratorCreateView.as_view(), name='create_collaborator'),
    path('edit-collaborator/<int:pk>', CollaboratorEditView.as_view(), name='edit_collaborator'),
    path('delete-collaborator/<int:pk>', CollaboratorDeleteView.as_view(), name='delete_collaborator'),
    path('detail-collaborator/<int:pk>', CollaboratorDetailView.as_view(), name='detail_collaborator'),
]
