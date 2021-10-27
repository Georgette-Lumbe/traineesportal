from django.shortcuts import render
from . forms import Notes, NotesForm
from django.contrib import messages
from django.views import generic, View

# Views


def homelist(request):
    """
    Create homelist view
    """
    return render(request, 'index.html')


def notes(request):
    """
    Create notes view
    """
    if request.method == "POST":  # When the save button is clicked
        form = NotesForm(request.Post)
        if form.is_valid():
            notes = Notes(user=request.user, title=request.POST['title'], description=request.POST['description'])
            notes.save()
            # Message when the note is added
            messages.success(request, f"Note added form {request.user.username} successfully!")
        else:
            form = NotesForm()

    notes = Notes.objects.filter(user=request.user)
    context = {'notes': notes, 'form': form}
    return render(request, 'notes.html', context)


def delete_note(request, pk=None):  # Delete note
    Notes.objects.get(id=pk).delete()
    return redirect("notes")


class NotesDetailView(generic.DetailView):
    model = Notes
