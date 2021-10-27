from django.urls import path
from blog import views


urlpatterns = [
    path('', views.homelist, name='homelist'),
    path('notes', views.notes, name='notes'),
    path('delete_note/<int:pk>', views.delete_note, name='delete_note'),
    path('notes_details/<int:pk>', views.NotesDetailView.as_view(),
         name='notes-detail'),

    path('assignments', views.assignments, name='assignments'),
    path('update_assignment/<int:pk>', views.update_assignment,
         name='update-assignment'),
    path('delete_assignment/<int:pk>', views.delete_assignment,
         name='delete-assignment'),
]
