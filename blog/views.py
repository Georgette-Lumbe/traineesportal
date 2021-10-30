from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views import generic
from . forms import Notes, NotesForm, AssignmentForm, TaskForm, CommentForm
from . models import Assignments, Tasks, Post

# Views


def homelist(request):
    """
    Create homelist view
    """
    posts = Post.objects.filter()  # Get the post id
    context = {
        'posts': posts,
        }
    return render(request, 'index.html', context)


@login_required
def notes(request):
    """
    Create notes view
    """
    if request.method == 'POST':  # When the save button is clicked
        form = NotesForm(request.Post)
        if form.is_valid():  # If the value is valid
            note = Notes(
                user=request.user,
                title=request.POST['title'],
                description=request.POST['description']
            )
            note.save()
            # Message when the note is added
            messages.success(request, f"Note from {request.user.username}"
                             " successfully added!")
    else:
        form = NotesForm()

    note = Notes.objects.filter(user=request.user)
    context = {'notes': notes, 'form': form}
    return render(request, 'notes.html', context)


def delete_note(request, pk=None):  # Delete note
    Notes.objects.get(id=pk).delete()
    return redirect("notes")


class NotesDetailView(generic.DetailView):
    model = Notes


@login_required
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

            assignment = Assignments(
                user=request.user,
                subject=request.POST['subject'],
                title=request.POST['title'],
                description=request.POST['description'],
                due=request.POST['due'],
                is_finished=finished
            )
            assignment.save()
            # Message when the assignment is added
            messages.success(request, f"Assignmnt from {request.user.username}"
                             " successfully added!")
    else:
        form = AssignmentForm()  # If the method is not POST

    assignment = Assignments.objects.filter(user=request.user)
    # When to notify the all assignments finished msg
    if len(assignment) == 0:
        assignment_done = True
    else:
        assignment_done = False

    context = {
            'assignments': assignments,
            'assignment_done': assignment_done,
            'form': form
    }

    return render(request, 'assignments.html', context)


def update_assignment(request, post_id):
    """
        When user hits checkbox
        to mark assignment as completed
    """
    assignment = Assignments.objects.get(pk=post_id)
    if assignment.is_finished is True:   # When user hits checkbox
        assignment.is_finished = False
    else:
        assignment.is_finished = True
    assignment.save()
    return redirect('assignment')


def delete_assignment(request, pk=None):  # Delete assignment
    Assignments.objects.get(id=pk).delete()
    return redirect('assignments')


@login_required
def tasks(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            try:
                finished = request.POST['is_finished']
                if finished == 'on':
                    finished = True
                else:
                    finished = False
            except:
                finished = False
            task = Tasks(
                user=request.user,
                title=request.POST['title'],
                is_finished=finished
            )
            task.save()  # Save to database
            # Message when the assignment is added
            messages.success(request, f"Task from {request.user.username}"
                             " successfully added!")
    else:
        form = TaskForm()

    task = Tasks.objects.filter(user=request.user)  # Display title on table
    if len(task) == 0:
        task_done = True
    else:
        task_done = False
    context = {
                'tasks': tasks,
                'form': form,
                'task_done': task_done
    }
    return render(request, 'tasks.html', context)


def post_one(request, post_id):
    post = Post.objects.get(pk=post_id)
    comments = post.comments.filter().order_by("-created_on")
    context = {
        "post": post,
        "comments": comments,
        "comment_form": CommentForm()
        }

    return render(request, 'post_one.html', context)


@login_required
def profile(request):
    """
    A view to return the user's profile page
    """
    assignments = Assignments.objects.filter(
                    is_finished=False, user=request.user)
    tasks = Tasks.objects.filter(is_finished=False, user=request.user)
    if len(assignments) == 0:
        assignment_done = True
    else:
        assignment_done = False
    if len(tasks) == 0:
        task_done = True
    else:
        task_done = False
    context = {
        'assignments': assignments,
        'tasks': tasks,
        'assignment_done': assignment_done,
        'task_done': task_done
    }

    return render(request, 'profile.html', context)
