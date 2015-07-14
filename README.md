# KungFuPanda_SettaluriKarthikSriharsha
This is humble attempt to solve the memory loss of Mr. Kung Fu Panda by using GoogleV3 API coded in Geopy library. The solution includes the following :

1) Use of Geopy (Geographical Python Library) supporting GoogleV3 api

2) List of Methods used :

a) getCordinatesForPlace() -- 
For given place, the function returns relevant latitude and longtiude cordinates
b) getPlaceFromCordinates() -- 
For given set of cordinates, the function returns relevant address location
c) generateCordinates() -- 
This generates a set of 5-10 cordinates in the range of (given_latitude-5,given_longitude-5)(given_latitude+5,given_longitude+5)
d) calculateNearestPlace() -- 
This calculates the distance of cordinates generated from c) and returns the minimum value address.
