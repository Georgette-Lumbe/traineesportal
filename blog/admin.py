from django.contrib import admin
from . models import Notes, Assignments, Tasks

# Models Registration

admin.site.register(Notes)
admin.site.register(Assignments)
admin.site.register(Tasks)
