from django import forms

from scraping.models import *


class FindForm(forms.Form):
    city = forms.ModelChoiceField(queryset=City.objects.all(),
                                  to_field_name="name", required=False,
                                  widget=forms.Select(attrs={'class': 'form-control'}),
                                  label='Город')
    language = forms.ModelChoiceField(queryset=Language.objects.all(),
                                      to_field_name="name", required=False,
                                      widget=forms.Select(attrs={'class': 'form-control'}),
                                      label='Язык программирования')
