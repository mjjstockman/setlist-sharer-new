from django import forms
from .models import Setlist


class SetlistForm(forms.ModelForm):
    # gig = forms.CharField(initial=2)
    class Meta:
        model = Setlist
        fields = ['gig', 'song']
        widgets = {'gig': forms.HiddenInput()}

class EditForm(forms.ModelForm):
    class Meta:
        model = Setlist
        fields = ['song']