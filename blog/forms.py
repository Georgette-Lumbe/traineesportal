from django import forms
from . models import Notes, Assignments, Tasks

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
    Map the Assignmentform
    """
    class Meta:
        model = Assignments
        widgets = {'due': DateInput()}
        fields = ['subject', 'title', 'description', 'due', 'is_finished']


class TaskForm(forms.ModelForm):
    """
    Map the Taskform
    """
    class Meta:
        model = Tasks
        fields = ['title', 'is_finished']

