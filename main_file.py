"This is the file that takes info for the functions to run. "
"This includes the observers position in lat, long and elevation(m), timestamp of the ROO image, RA and DEC of the suspected satellites in the image and the angular distance threshold"

from set_telescope_position import set_telescope_position
from image_reader import fits_image_reader
from tle_parser import tle_reader
from Propagator_and_matcher import satellite_propagator

# First function: Telescope location in latitude, longitude and elevation(m)
telescope_lat =  -37.680589141
telescope_long = 145.061634327
telescope_elevation = 155.083

telescope_position = set_telescope_position(telescope_lat, telescope_long, telescope_elevation)

# Image metadata 
image_time, image_RA, image_DEC = fits_image_reader()
image_RA_and_DEC = [image_RA, image_DEC]

# Importing TLE data
sats_by_name = tle_reader()

# Orbit propagation and matching
possible_satellites = satellite_propagator(telescope_position, image_time, image_RA_and_DEC, sats_by_name, angular_distance_limit=0.05)

print ("Close matches:", possible_satellites)

#test on other images
