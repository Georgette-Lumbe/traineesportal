from django.contrib import admin
from . models import Notes, Assignments, Tasks, Post
from django_summernote.admin import SummernoteModelAdmin

# Models Registration


@admin.register(Post)       # decorator
class PostAdmin(SummernoteModelAdmin):
    """
    Make blog writing easy
    """
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content')
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title']
    list_filter = ('status', 'created_on')


admin.site.register(Notes)
admin.site.register(Assignments)
admin.site.register(Tasks)
