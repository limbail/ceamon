from django import forms
from ceamon.models import sapnode, StatusModel
from django.forms import ModelForm

class OverviewForm(ModelForm):
    class Meta:
        model = StatusModel
        fields = ['system', 'status_id', 'status', 'comment']

