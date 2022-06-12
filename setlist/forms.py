from django import forms
from .models import Setlist
from home.models import Gig


class SetlistForm(forms.ModelForm):
    class Meta:
        model = Setlist
        fields = ['gig', 'song', 'author']
        widgets = {
            'gig': forms.HiddenInput(),
            'author': forms.HiddenInput(),
            }

class EditForm(forms.ModelForm):
    class Meta:
        model = Setlist
        fields = ['song']

class AddImageForm(forms.ModelForm):
    class Meta:
        model = Gig
        fields = ['featured_image']