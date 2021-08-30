from django import forms
from .models import Mesurment

class MesurmentModelForm(forms.ModelForm):
    class Meta:
        model = Mesurment
        fields = ('distination', )