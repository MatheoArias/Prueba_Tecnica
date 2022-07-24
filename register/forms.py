from django import forms
from .models import State,City,Citizen


class FormState(forms.ModelForm):
    class Meta:
        model=State
        fields='__all__'
        exclude=()


class FormCity(forms.ModelForm):
    class Meta:
        model=City
        fields='__all__'
        exclude=()


class FormCitizen(forms.ModelForm):
    class Meta:
        model=Citizen
        fields='__all__'

        
        
