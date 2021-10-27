from django.shortcuts import render, redirect
from . forms import Notes, NotesForm, AssignmentForm
from django.contrib import messages
from django.views import generic
from . models import Assignments, Tasks

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
        if form.is_valid():  # If the value is valid
            notes = Notes(user=request.user, title=request.POST['title'],
                          description=request.POST['description'])
            notes.save()
            # Message when the note is added
            messages.success(request, f"Note from {request.user.username}"
                             " successfully added!")
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
    if request.method == 'POST':  # If the method is POST
        form = AssignmentForm(request.POST)
        if form.is_valid():
            try:
                finished = request.POST['is_finished']
                if finished == 'on':
                    finished = True
                else:
                    finished = False
            except:
                finished = False

            assignments = Assignments(
                user=request.user,
                subject=request.POST['subject'],
                title=request.POST['title'],
                description=request.POST['description'],
                due=request.POST['due'],
                is_finished=finished
            )
            assignments.save()
            # Message when the assignment is added
            messages.success(request, f"Assignmnt from {request.user.username}"
                             " successfully added!")
    else:
        form = AssignmentForm()  # If the method is not POST

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


def update_assignment(request, pk=None):
    """
        When user hits checkbox
        to mark assignment as completed
        """
    assignments = Assignments.objects.get(id=pk)
    if assignments.is_finished is True:   # When user hits checkbox
        assignments.is_finished = False
    else:
        assignments.is_finished = True
    assignments.save()
    return redirect('assignment')


def delete_assignment(request, pk=None):  # Delete assignment
    Assignments.objects.get(id=pk).delete()
    return redirect('assignments')


def tasks(request):
    tasks = Tasks.objects.filter(user=request.user)  # Display title on table
    context = {
        'tasks': tasks
    }
    return render(request, 'tasks.html', context)

