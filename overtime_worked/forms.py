from django.forms import ModelForm
from .models import OvertimeWorked


class OvertimeWorkedForm(ModelForm):

    class Meta:
        model = OvertimeWorked
        fields = '__all__'
   
    def __init__(self, *args, **kwargs):
        super(OvertimeWorkedForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
      