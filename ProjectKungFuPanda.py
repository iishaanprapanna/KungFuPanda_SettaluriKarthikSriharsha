from geopy.geocoders import Nominatim
from geopy.geocoders import GoogleV3

def generateCordinates(cordinates):
    '''
    Note : This function tries to generate a spherial or elliptical globe
    by adding +5 and -5 to the supplied coordinates and thus generates say
    for example : 10 latitude and 10 longitude values. These values are
    compared for computing the distance between supplied coordinates and thus
    find the minimum distance among them. The minimum value computed so far is
    the return value.
    '''
    return None
def calculateNearestPlace(cordinates,geolocator):
    mylatlist = []
    mylonglist = []
    (latt,longt) = cordinates.split(",")
    print latt,longt
    (mylatlist,mylonglist)= generateCordinates(cordinates)

    
def getPlaceFromCordinates(cordinates,geolocator):
    myLoc = geolocator.reverse((str(cordinates)),exactly_one=True)
    if myLoc is not None:
        return myLoc
    elif:
        print "myLoc is None"
        return calculateNearestPlace(cordinates,geolocator)
        



def getCordinatesFromPlace(place,geolocator):
    address,(myLong,myLat) = geolocator.geocode(place)
    return myLong,myLat

    
def main():
    print "... Start Initiliazing Geolocator based on GoogleV3 ..."
    geolocator = GoogleV3()
    print geolocator
    
    print "... Done Initializing ..."

    case = map(int,raw_input())
    #print case
    if case[0] == 1:
        #print "... Enter cordinates ..."
        cordinates = raw_input()
        if cordinates is not None:
            #print cordinates
            #print "... Getting the place information from cordinates ..."
            print getPlaceFromCordinates(cordinates,geolocator)
    elif case[0] == 2:
        #print "... Enter the place ..."
        place = raw_input()
        #print place
        #print "... Gettings Cordinates of the place ..."
        print getCordinatesFromPlace(place,geolocator)
    

if __name__ == "__main__":
    main()
