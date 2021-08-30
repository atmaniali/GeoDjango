from django.shortcuts import render, get_object_or_404
from .models import Mesurment
from .forms import MesurmentModelForm

# Create your views here.

def calculate_distance_view(request):
    template_name = 'mesurments/index.html'
    context = {}
    object = get_object_or_404(Mesurment, id = 1)
    context["obj"] = object
    return render(request, template_name, context)
