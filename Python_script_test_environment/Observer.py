# Importing the Topos object from the Skyfield API so we can do computations relative to a position on the Earth.    
from skyfield.api import Topos
# We now define a function using the topos object to assign a latitude and a longitude and an elevation to where the telescope is. 
def get_observer_location(lat, lon, elevation_m=0):
    return Topos(latitude_degrees=lat, longitude_degrees=lon, elevation_m=elevation_m)
# ROO Observatory position obs = [-37.680589141, 145.061634327, 0.155083]  #surveying results for ROO (latitude, longitude and elevation (in Kilometres))