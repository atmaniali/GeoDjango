def get_center_location(latA, lonA, latB= None, lonB= None):
    cord = (latA, lonA)
    if latB :
        lat = (latA+latB)/2
        long = ((lonA+lonB))/2
        cord = [lat, long]
    return cord

latA  = 37.751  
lonA = -97.822
latB= 35.7032751
lonB= -0.6492976

a = get_center_location(latA, lonA)
print (a)
b = get_center_location(latA, lonA, latB , lonB)
print (b)