from django.shortcuts import render, get_object_or_404
from .models import Mesurment
from .forms import MesurmentModelForm
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from .utils import (get_geo, get_center_location, get_zom)
import folium

# Create your views here.

def calculate_distance_view(request):
    # initialisation of render
    template_name = 'mesurments/main.html'
    context = {}
    distance_ = None
    distination = None
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
    # location cordinate
    loca_latit = lat
    loca_long = lon

    pointA = (loca_latit, loca_long)

    # initiale foluim maps
    m = folium.Map(width = 800, height = 500, location = get_center_location(loca_latit, loca_long), zoom_start = 100)
    # location marker
    folium.Marker([loca_latit,loca_long], tooltip = "click here for more", popup = city['city'], icon = folium.Icon(color= 'purple')).add_to(m)

    if form.is_valid():
        instance = form.save(commit = False)
        distination_ = form.cleaned_data.get('distination')
        distination = geolocator.geocode(distination_)

        print(distination)


        # distination cordinate
        dist_latit = distination.latitude
        dist_long = distination.longitude

        pointB = (dist_latit, dist_long)
        # distance calculated
        distance_ = round(geodesic(pointA, pointB).km, 2)

        
        # folium mup modification
        m = folium.Map(width = 800, height = 500, location = get_center_location(loca_latit, loca_long, dist_latit, dist_long), zoom_start = get_zom(distance_))
        # location marker
        folium.Marker([loca_latit,loca_long], tooltip = "click here for more", popup = city['city'], icon = folium.Icon(color= 'purple')).add_to(m)
        # distination marker
        folium.Marker([dist_latit,dist_long], tooltip = "click here for more", popup = distination, icon = folium.Icon(color= 'red', icon = 'cloud')).add_to(m)

        #draw line between location and distination
        folium.PolyLine(locations = [pointA, pointB], weight = 5, color = 'blue').add_to(m)


        instance.location = location
        instance.distance = distance_
        instance.save()

    m = m._repr_html_()    

    # context
    context["obj"] = object
    context["form"] = form   
    context["maps"] = m 
    context['distance'] = distance_  
    context['distination'] = distination 

    return render(request, template_name, context)
