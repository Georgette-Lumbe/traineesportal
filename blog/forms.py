from django import forms
from . models import Notes

# Forms


class NotesForm(forms.ModelForm):
    """Map the Notesform"""
    class Meta:
        model = Notes()
        fields = ['title', 'description']
