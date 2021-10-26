from django.shortcuts import render
from django.views import generic

# Create your views here.


class HomeList(generic.ListView):
    """
    Create HomeList view
    """
    def home(request):
        return render(request, 'index.html')
