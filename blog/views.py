from django.shortcuts import render
from . forms import Notes, NotesForm, AssignmentForm
from django.contrib import messages
from django.views import generic
from . models import Assignments

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


def assignments(request):
    """
    Create assignments view
    """
    form = AssignmentForm()
    assignments = Assignments.objects.filter(user=request.user)
    # When to notify the all assignments finished msg
    if len(assignments) == 0:
        assignment_done = True
    else:
        assignment_done = False

    context = {
            'assignments': assignments,
            'assignments_done': assignment_done,
            'form': form
    }

    return render(request, 'assignments.html', context)
