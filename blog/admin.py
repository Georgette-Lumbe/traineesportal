from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from . models import Notes, Assignments, Tasks, Post, Comment


# Models Registration


@admin.register(Post)       # decorator
class PostAdmin(SummernoteModelAdmin):
    """
    Make blog writing easy
    """
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title']
    list_filter = ('status', 'created_on')
    summernote_fields = ('content',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Manage Comments
    """
    list_display = ('name', 'body', 'post', 'created_on')
    search_fields = ('name', 'email', 'body')


@admin.register(Notes)
class NotesAdmin(admin.ModelAdmin):
    """
    Manage Notes
    """
    list_display = ('title', 'description')
    search_fields = ('title', 'description')
    list_filter = ('title', 'description')


@admin.register(Tasks)
class TasksAdmin(admin.ModelAdmin):
    """
    Manage Notes
    """
    list_display = ('title', 'is_finished')
    list_filter = ('title', 'is_finished')


@admin.register(Assignments)
class AssignmentsAdmin(admin.ModelAdmin):
    """
    Manage Assignments
    """
    list_display = ('title', 'subject', 'description', 'due', 'is_finished')
    list_filter = ('title', 'is_finished')
    search_fields = ('title', 'subject')
