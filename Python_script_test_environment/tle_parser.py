'Program to pull satellite TLE data from the web to use as a source to compare the RA and DEC agaisnt the RA and DEC'
'of the image taken of the space object'

# Importing urllib fucntions so that we can extract information from the web
import urllib.request
import urllib.error as urlerror
# We now have a function that pulls the required info from celestrack and writes it as a txt file
# Importantly accessing this website and downloading from it too many times will lead to you getting suspended for 2 hours.
def TLE_parser_from_web():
    
    #Celestrack URL for TLE on all actively trached satellites should encorporate methods to update TLE collection after a
    #number of days to ensure accurate data to compare with ROO images
    url = "https://celestrak.org/NORAD/elements/gp.php?GROUP=active&FORMAT=tle"
    
    #From the webpage, writing a txt file of all TLE data
    try:
        tle_page = urllib.request.urlopen(url).read().decode()
        tle_file = open('tle_data.txt', 'w')
        tle_file.write(tle_page)
        tle_file.close
    
    except urlerror as e:
        print (e)