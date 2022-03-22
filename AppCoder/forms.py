from pyexpat import model
from django import forms

class input_auto(forms.Form):
    marca = forms.CharField(max_length=40)
    chasis = forms.CharField(max_length=40)
    tipo = forms.CharField(max_length=4)
    motor = forms.CharField(max_length=40)

class BusquedaAuto(forms.Form):
    partial_marca = forms.CharField(label = 'Buscador', max_length=40)
