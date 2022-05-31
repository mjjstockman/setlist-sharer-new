from django import forms
from .models import Setlist


class SetlistForm(forms.ModelForm):
    class Meta:
        model = Setlist
        fields = ['song']

class EditForm(forms.ModelForm):
    class Meta:
        model = Setlist
        fields = ['song']