from django.forms import *
from django.db import models
from core.erp.models import *

class CategoryForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-cotrol'
            form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['name'].widget.attrs['autofocus'] = True
    class Meta:
        model = Category
        fields = '__all__'
        widgets = {
            'name': TextInput(
                attrs={
                    'placeholder' : 'Ingrese un nombre',
                }
            ),
            'desc': Textarea(
                attrs={
                    'placeholder' : 'Ingrese una descripcion',
                    'rows': 3,
                    'cols': 3
                }
            )
        }
