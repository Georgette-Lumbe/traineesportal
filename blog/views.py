from django.shortcuts import render
from . forms import Notes, NotesForm
# from . models import Notes

# Views


def homelist(request):
    """
    Create homelist view
    """
    return render(request, 'index.html')


def notesdetails(request):
    """
    Create notes view
    """

    notes = Notes.objects.filter(user=request.user)
    context = {'notes': notes, 'form': form}
    return render(request, 'notes.html', context)
