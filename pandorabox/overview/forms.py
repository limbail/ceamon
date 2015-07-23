from django import forms
from ceamon.models import sapnode
from django.forms import ModelForm

class OverviewForm(ModelForm):

    class Meta:
        model = sapnode
        fields = ['hostname','sid']

