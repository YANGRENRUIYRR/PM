from django import forms
from .models import Website,Username
class WebsiteForm(forms.ModelForm):
    class Meta:
        model = Website
        fields = ['text']
        labels = {'text': ''}
class UsernameForm(forms.ModelForm):
    class Meta:
        model = Username
        fields = ['text','text2']
        labels = {'text': '','text2':''}
        widgets = {'text':'','text2':''}