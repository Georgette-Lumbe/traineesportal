"""Import Modules"""
from django import forms
from . models import Notes, Assignments, Tasks, Comment

# Forms


class NotesForm(forms.ModelForm):
    """
    Map the Notesform
    """
    class Meta:
        """
        How the form should display
        """
        model = Notes
        fields = ['title', 'description']


class DateInput(forms.DateInput):
    input_type = 'date'


class AssignmentForm(forms.ModelForm):
    """
    Map the Assignmentform
    """
    class Meta:
        """
        How the form should display
        """
        model = Assignments
        widgets = {'due': DateInput()}
        fields = ['subject', 'title', 'description', 'due', 'is_finished']


class TaskForm(forms.ModelForm):
    """
    Map the Taskform
    """
    class Meta:
        """
        How the form should display
        """
        model = Tasks
        fields = ['title', 'is_finished']


class CommentForm(forms.ModelForm):
    """
    Map the Commentform
    """
    class Meta:
        """
        How the form should display
        """
        model = Comment
        fields = ('body',)
