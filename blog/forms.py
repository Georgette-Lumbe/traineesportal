from django import forms
from . models import Notes, Assignments

# Forms


class NotesForm(forms.ModelForm):
    """
    Map the Notesform
    """
    class Meta:
        model = Notes
        fields = ['title', 'description']


class DateInput(forms.DateInput):
    input_type = 'date'


class AssignmentForm(forms.ModelForm):
    """
    Map the Notesform
    """
    class Meta:
        model = Assignments
        widgets = {'due': DateInput()}
        fields = ['subject', 'title', 'description', 'due', 'is_finished']
