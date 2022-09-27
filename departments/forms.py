from django.forms import ModelForm
from .models import Department


class DepartmentForm(ModelForm):

    class Meta:
        model = Department
        fields = '__all__'
   
    def __init__(self, *args, **kwargs):
        super(DepartmentForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
