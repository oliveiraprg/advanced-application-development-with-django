from django.forms import ModelForm, DateField
from .models import Collaborator
from departments.models import Department


class CollaboratorForm(ModelForm):

    class Meta:
        model = Collaborator
        fields = ['name', 'position', 'salary','departments',
                  'status_collaborator', 'start_in_company', 'fired_of_company']
   
    def __init__(self, user, *args, **kwargs):
        super(CollaboratorForm, self).__init__(*args, **kwargs)
        self.fields['departments'].queryset = Department.objects.filter(company=user.collaborator.company)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})