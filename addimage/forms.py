from django import forms
from home.models import Gig


class AddImageForm(forms.ModelForm):
    class Meta:
        model = Gig
        fields = ['featured_image']
