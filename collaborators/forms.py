from django.forms import ModelForm
from .models import Collaborator
from departments.models import Department


class CollaboratorForm(ModelForm):

    class Meta:
        model = Collaborator
        fields = ['name', 'position', 'salary', 'departments']
   
    def __init__(self, user, *args, **kwargs):
        super(CollaboratorForm, self).__init__(*args, **kwargs)
        self.fields['departments'].queryset = Department.objects.filter(company=user.collaborator.company)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
      