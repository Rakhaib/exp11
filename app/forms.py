from django import forms
from .models import abc


class UserForm(forms.ModelForm):
    class Meta:
        model=abc
        fields=[
            'name','age'
        ]