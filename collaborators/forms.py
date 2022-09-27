from django.forms import ModelForm
from .models import Collaborator


class CollaboratorForm(ModelForm):

    class Meta:
        model = Collaborator
        fields = '__all__'
   
    def __init__(self, *args, **kwargs):
        super(CollaboratorForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
      