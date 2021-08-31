from django.contrib.gis.geoip2 import GeoIP2


# Helper function

def get_geo(ip) :
    g = GeoIP2()
    cuntry = g.country(ip)
    city = g.city(ip)
    lat , long = g.lat_lon(ip)
    return cuntry, city, lat, long


def get_center_location(latA, lonA, latB= None, lonB= None):
    cord = (latA, lonA)
    if latB :
        cord = [(latA+latB)/2, (lonA+lonB)/2]
    return cord

def  get_zom(distance):
    if distance <= 100:
        return 8
    elif distance > 100 and distance < 5000 : 
        return 4
    else: return 2     

def get_ip_addres(request):
    
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADD') 
    return ip     

