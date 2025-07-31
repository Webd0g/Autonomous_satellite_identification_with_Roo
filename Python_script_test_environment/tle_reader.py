
from skyfield.api import load
def tle_reader():
    sat_info =[]
    hand = open('tle_data.txt', 'r')
    lines = hand.readlines()
    for l in range(0, len(lines), 3):
        name = lines[l].strip
        TLE_line_1 = lines[l+1].strip
        TLE_line_2 = lines[l+2].strip
        satellite = load.tle_file(TLE_info = [TLE_line_1, TLE_line_2], satellite_name = name)[0]
        sat_info[name] = satellite
    return sat_info
tle_reader()