from django import forms
from .models import Record

class CreateRecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['photo', 'full_name', 'email', 'mobile', 'date_of_birth']
        
        widgets = {
            'date_of_birth': forms.DateInput(attrs={
                'type': 'date',
                'id': 'id_date_of_birth',
                'class': 'form-control'  # Optional: Use Bootstrap class for styling
            }),
        }