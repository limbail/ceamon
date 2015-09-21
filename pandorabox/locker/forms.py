from django import forms
from .models import locker
from django.forms import ModelForm

class LockerForm(ModelForm):
    #title = forms.CharField(max_length=40, required=True)

    class Meta:
        #title = forms.CharField(max_length=40, required=True)

        model = locker
        fields = ['title', 'e_username', 'e_password', 'e_url', 'e_notes']
