'Python program that is used to determine the position of the observations using ROO to use in a larger function to'
'determine the identity of a object detected by ROO'

# Importing the Topos object from the Skyfield API so we can do computations relative to a position on the Earth.
from skyfield.api import Topos
# We now define a function using the topos object to assign a latitude and a longitude and an elevation to where the telescope is.
def set_telescope_position(telescope_lat, telescope_long, telescope_elevation):
    return Topos(latitude_degrees = telescope_lat, longitude_degrees = telescope_long, elevation_m = telescope_elevation)
# ROO Observatory position obs = [-37.680589141, 145.061634327, 0.155083]  #surveying results for ROO (latitude, longitude and elevation (in Kilometres))