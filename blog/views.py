"""Import Modules"""
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views import generic
from . forms import Notes, NotesForm, AssignmentForm, TaskForm, CommentForm
from . models import Assignments, Tasks, Post

# Views


def homelist(request):
    """
    Create home view
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
        form = NotesForm(request.POST)
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
    context = {'notes': note, 'form': form}
    return render(request, 'notes.html', context)


def delete_note(_request, pk=None):
    """
    Delete note when user hits the trash button
    """
    Notes.objects.get(id=pk).delete()
    return redirect("notes")


class NotesDetailView(generic.DetailView):
    """
    Display note detail after user create a note
    """
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
            except KeyError:
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
            messages.success(request, f"Assignment from {request.user.username}"  # noqa
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
            'assignments': assignment,
            'assignment_done': assignment_done,
            'form': form
    }

    return render(request, 'assignments.html', context)


def update_assignment(_request, pk=None):
    """
        When user hits checkbox
        to mark assignment as completed
    """
    assignment = Assignments.objects.get(id=pk)
    assignment.is_finished = True if assignment.is_finished is False else False
    assignment.save()
    return redirect('assignments')


def delete_assignment(_request, pk=None):
    """
    Delete assignment when user hits the trash button
    """
    Assignments.objects.get(id=pk).delete()
    return redirect('assignments')


@login_required
def tasks(request):
    """
    Create Task view
    """
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            try:
                finished = request.POST['is_finished']
                if finished == 'on':
                    finished = True
                else:
                    finished = False
            except KeyError:
                finished = False
            task = Tasks(
                user=request.user,
                title=request.POST['title'],
                is_finished=finished
            )
            task.save()  # Save to the database
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
                'tasks': task,
                'form': form,
                'task_done': task_done
    }
    return render(request, 'tasks.html', context)


def update_task(_request, pk=None):
    """
        When user hits checkbox
        to mark task as completed
    """
    task = Tasks.objects.get(id=pk)
    task.is_finished = True if task.is_finished is False else False
    task.save()
    return redirect('tasks')


def delete_task(_request, pk=None):
    """
    Delete task when user hits the trash button
    """
    Tasks.objects.get(id=pk).delete()
    return redirect('tasks')


def post_details(request, post_id):
    """
    Create Post details view
    """
    post = Post.objects.get(pk=post_id)
    comments = post.comments.order_by("-created_on")
    form = None
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.instance.email = request.user.email
            form.instance.name = request.user.username
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
    else:
        form = CommentForm()

    print(type(comments))
    context = {
        "post": post,
        "comments": comments,
        "comment": True,
        "form": form,
        }

    return render(request, 'post_details.html', context)


@login_required
def profile(request):
    """
    Create a profile view
    """
    assignment = Assignments.objects.filter(
                    is_finished=False, user=request.user)
    task = Tasks.objects.filter(is_finished=False, user=request.user)
    if len(assignment) == 0:
        assignment_done = True
    else:
        assignment_done = False
    if len(task) == 0:
        task_done = True
    else:
        task_done = False
    context = {
        'assignments': assignment,
        'tasks': task,
        'assignment_done': assignment_done,
        'task_done': task_done
    }

    return render(request, 'profile.html', context)
