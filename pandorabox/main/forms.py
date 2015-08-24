from django import forms
from locker.models import locker

class LockerForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="title")
    username = forms.CharField(max_length=128, help_text="username")
    password = forms.CharField(max_length=128, help_text="password")
    url = forms.CharField(max_length=128, help_text="url")
    notes = forms.CharField(max_length=128, help_text="notes")

    class Meta:
        model = locker
        fields = ('title', 'username', 'password', 'url', 'notes', )
