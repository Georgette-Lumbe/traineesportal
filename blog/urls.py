"""Import Modules"""
from django.urls import path
from blog import views


urlpatterns = [
    path('', views.homelist, name='homelist'),    # Home URL

    path('notes', views.notes, name='notes'),     # Notes URL
    path('delete_note/<int:pk>', views.delete_note, name='delete_note'),
    path('notes_detail/<int:note_id>', views.notes_detail, name='notes_detail'),  # noqa

    path('assignments', views.assignments, name='assignments'),  # Assignments
    path('delete_assignment/<int:pk>', views.delete_assignment,
         name='delete-assignment'),
    path('update_assignment/<int:pk>', views.update_assignment,
         name='update-assignment'),

    path('tasks', views.tasks, name='tasks'),     # Tasks URL
    path('delete_task/<int:pk>', views.delete_task,
         name='delete-task'),
    path('update_task/<int:pk>', views.update_task,
         name='update-task'),

    path('post_details/<int:post_id>', views.post_details, name='post_details'),  # noqa

    path('profile/', views.profile, name='profile'),  # Profile URL
]
