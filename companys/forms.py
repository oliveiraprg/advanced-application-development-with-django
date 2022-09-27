from django.forms import ModelForm
from .models import Company


class CompanyForm(ModelForm):

    class Meta:
        model = Company
        fields = '__all__'
   
    def __init__(self, *args, **kwargs):
        super(CompanyForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
      