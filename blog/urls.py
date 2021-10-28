from django.urls import path
from blog import views


urlpatterns = [
    path('', views.homelist, name='homelist'),    # Home URL

    path('notes', views.notes, name='notes'),     # Notes URL
    path('delete_note/<int:pk>', views.delete_note, name='delete_note'),
    path('notes_details/<int:pk>', views.NotesDetailView.as_view(),
         name='notes-detail'),

    path('assignments', views.assignments, name='assignments'),  # Assignments
    path('delete_assignment/<int:pk>', views.delete_assignment,
         name='delete-assignment'),
    path('update_assignment/<int:pk>', views.update_assignment,
         name='update_assignment'),

    path('tasks', views.tasks, name='tasks'),     # tasks URL

    # path('post_one', views.post_one, name='post_one'),
    path('<slug:slug>/', views.PostOne.as_view(), name='post_one'),  # Post1URL
]
