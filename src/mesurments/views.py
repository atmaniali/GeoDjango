from django.shortcuts import render, get_object_or_404
from .models import Mesurment
from .forms import MesurmentModelForm
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from .utils import get_geo

# Create your views here.

def calculate_distance_view(request):
    # initialisation of render
    template_name = 'mesurments/main.html'
    context = {}
    # methodes
    object = get_object_or_404(Mesurment, id = 1)
    form = MesurmentModelForm(request.POST or None)

    geolocator = Nominatim(user_agent="mesurments")
    # ip from california
    ip = "72.14.207.99"
    country, city, lat , lon = get_geo(ip)
    location = geolocator.geocode(city)

    print("country", country)
    print("city", city)
    print("lat , lon", lat , lon)
    print("### location ", location)

    loca_latit = lat
    loca_long = lon

    pointA = (loca_latit, loca_long)

    if form.is_valid():
        instance = form.save(commit = False)

        distination_ = form.cleaned_data.get('distination')
        distination = geolocator.geocode(distination_)

        print(distination)


        dist_latit = distination.latitude
        dist_long = distination.longitude

        pointB = (dist_latit,dist_long)

        distance_ = round(geodesic(pointA, pointB).km, 2)
        instance.location = location
        instance.distance = distance_
        instance.save()
    # context
    context["obj"] = object
    context["form"] = form       

    return render(request, template_name, context)
