from django.shortcuts import render, get_object_or_404
from .models import Mesurment
from .forms import MesurmentModelForm

# Create your views here.

def calculate_distance_view(request):
    # initialisation of render
    template_name = 'mesurments/main.html'
    context = {}
    # methodes
    object = get_object_or_404(Mesurment, id = 1)
    form = MesurmentModelForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit = False)
        instance.distination = form.cleaned_data.get('distination')
        instance.location = 'San Francisco'
        instance.distance = 4000.00
        instance.save()
    # context
    context["obj"] = object
    context["form"] = form       

    return render(request, template_name, context)
