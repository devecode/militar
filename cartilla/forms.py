from django import forms

from .models import Cartilla

class CartillaForm(forms.ModelForm):
    class Meta:
        model=Cartilla
        fields=['clase','nombre','fecha_nacimiento','nacio','papa','mama','estado','ocupacion','leer_escribir','curp',
                'grado_maximo', 'domicilio', 'presidente', 'lugar']
        widget={'fecha_nacimiento':forms.DateInput()}
        exclude = ['fecha']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })