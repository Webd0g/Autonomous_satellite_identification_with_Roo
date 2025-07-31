'A program that reads and oragnises that TLE data into a format that can be used readily for the comparison process to identify the space object'

#Importing the load funtion from skyfield module in this case to take the organised TLE info and turn it into a tle_file object
from skyfield.api import load


def tle_reader():
    sat_info =[]
    hand = open('tle_data.txt', 'r')
    lines = hand.readlines()

    #Iterating through the TLE txt file in blocks of three to oragnise each satellites TLE data
    for l in range(0, len(lines), 3):
        name = lines[l].strip
        TLE_line_1 = lines[l+1].strip
        TLE_line_2 = lines[l+2].strip

        #loads the iterated info into a list and transforms the two line elements into Skyfield EarthSatellite objects which allows us to easily compute positions using this list.
        satellite = load.tle_file(TLE_info = [TLE_line_1, TLE_line_2], satellite_name = name)[0]
        sat_info[name] = satellite
    return sat_info