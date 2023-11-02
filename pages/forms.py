from django import forms
from .models import Letter


class LetterForm(forms.ModelForm):
    class Meta:
        model = Letter
        fields = ('displayed_name', 'message')
        widgets = {
            'displayed_name': forms.TextInput(attrs={'placeholder': 'Your Name'}),
            'message': forms.Textarea(attrs={'placeholder': 'Your Message'}),
        }
