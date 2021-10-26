from django.urls import path
from . import views


urlpatterns = [
    path('', views.homelist, name='homelist'),
    path('notes', views.notesdetails, name='notesdetails')
]
