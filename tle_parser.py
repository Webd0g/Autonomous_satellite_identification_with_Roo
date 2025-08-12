from skyfield.api import load
from skyfield.iokit import parse_tle_file

def tle_reader():

    ts = load.timescale()

    with load.open("tle_data.txt") as tle_data:
        satellites = list(parse_tle_file(tle_data, ts))
    
    sats_by_name = {sat.name: sat for sat in satellites}
    return sats_by_name

#source: https://ascl.net/1907.024