from django.forms import ModelForm, TextInput
from .models import Parsing 

class SubjectForm(ModelForm):
    class Meta:
        model = Parsing
        fields = ['search']

        widgets = {
            'search': TextInput(attrs={
                'class': 'main-input',
                'placeholder': 'Название товара',
                'type': 'text'
            })
        }
        