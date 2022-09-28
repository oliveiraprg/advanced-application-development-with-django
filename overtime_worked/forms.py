from django.forms import ModelForm
from .models import OvertimeWorked
from collaborators.models import Collaborator


class OvertimeWorkedForm(ModelForm):

    class Meta:
        model = OvertimeWorked
        fields = '__all__'
   
    def __init__(self, user, *args, **kwargs):
        super(OvertimeWorkedForm, self).__init__(*args, **kwargs)
        self.fields['owner'].queryset = Collaborator.objects.filter(company=user.collaborator.company)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

      