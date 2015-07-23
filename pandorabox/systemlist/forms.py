from django import forms

class modify_form(forms.Form):
    hostname = forms.CharField(max_length=30)
