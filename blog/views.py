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
    if request.method == "POST":  # When the save button is clicked
        form = NotesForm(request.Post)
        if form.is_valid():
            notes = Notes(user=request.user, title=request.POST['title'], description=request.POST['description'])
            notes.save()
            # Message when the note is added
            messages.success(request, f"Your note from {request.user.username} was successfully added!")
        else:
            form = NotesForm()

    notes = Notes.objects.filter(user=request.user)
    context = {'notes': notes, 'form': form}
    return render(request, 'notes.html', context)
