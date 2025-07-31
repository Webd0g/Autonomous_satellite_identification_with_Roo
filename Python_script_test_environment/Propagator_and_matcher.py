from skyfield.api import load
import numpy as np

def satellite_propagator (observer_location, sat_info, image_time, image_ra_and_dec, angular_distance_limit):
    satellite_matches = {}

    ts = load.timescale()
    t = ts.utc(image_time.year, image_time.month, image_time.day, image_time.hour, image_time.minute, image_time.second)

    for name, satellite in sat_info.items():
        difference = satellite - observer_location
        topocentric = difference.at(t)
        ra, dec, distance = topocentric.radec(epoch=t)

        angular_distance_from_TLE = np.arccos((np.sin(image_ra_and_dec[1])*np.sin(dec)+np.cos(image_ra_and_dec[1])*np.cos(dec)*np.cos(image_ra_and_dec[0]-ra)))

        if angular_distance_from_TLE < angular_distance_limit:
            satellite_matches[name] = angular_distance_from_TLE
    
    sorted_satellite_matches = {}
    
    for key in sorted(satellite_matches, key =satellite_matches.get):
        sorted_satellite_matches[key] = satellite_matches[key]
    
    return sorted_satellite_matches