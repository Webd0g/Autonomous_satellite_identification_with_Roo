'Orbit propagator program, this takes the TLE data from the previous programs and the time of the ROO images and propagates the satellites in the TLE list to where they should be at the image time'
'it then compares the angular distance between the space object using TLE RA and DEC and the ROO image object and returns a list of close matches.'

#Importing the load function to load skyfield specific objects, in this case it is the timescale object which lets us use skyfield time related functions
# We also import numpy for cos and sin functions for angular distance calculations
from skyfield.api import load
import numpy as np

def satellite_propagator (observer_location, sat_info, image_time, image_ra_and_dec, angular_distance_limit):
    satellite_matches = {}

    #loads timescale object so that we can use .at() and .utc()
    ts = load.timescale()
    t = ts.utc(image_time.year, image_time.month, image_time.day, image_time.hour, image_time.minute, image_time.second)

    #Iterates through each satellite info by the name of each satellite and uses info to determine angular distance between TLE RA and DEC and ROO image RA and DEC
    for name, satellite in sat_info.items():
        difference = satellite - observer_location
        topocentric = difference.at(t)
        ra, dec = topocentric.radec(epoch=t)

        angular_distance_from_TLE = np.arccos((np.sin(image_ra_and_dec[1])*np.sin(dec)+np.cos(image_ra_and_dec[1])*np.cos(dec)*np.cos(image_ra_and_dec[0]-ra)))

        #Angular distance comparison, this is one of the large issues what do we choose for cutoff?
        if angular_distance_from_TLE < angular_distance_limit:
            satellite_matches[name] = angular_distance_from_TLE
    
    sorted_satellite_matches = {}
    
    #Iterates through the matched satellites to sort the matches from closest to furthest away.
    for key in sorted(satellite_matches, key =satellite_matches.get):
        sorted_satellite_matches[key] = satellite_matches[key]
    
    #Returns close satellites
    return sorted_satellite_matches