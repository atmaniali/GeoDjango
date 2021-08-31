from django.contrib.gis.geoip2 import GeoIP2


# Helper function

def get_geo(ip) :
    g = GeoIP2()
    cuntry = g.country(ip)
    city = g.city(ip)
    lat , long = g.lat_lon(ip)
    return cuntry, city, lat, long


def get_center_location(latA, lonA, latB= None, lonB= None):
    cord = (latA,lonA)
    if latB & lonB:
        cord = [(latA)]
    return cord
