'Program to pull satellite TLE data from the web to use as a source to compare the RA and DEC against the RA and DEC'
'of the image taken of the space object'

# Importing urllib functions so that we can extract information from the web
import urllib.request
import urllib.error as urlerror
# We now have a function that pulls the required info from celestrack and writes it as a txt file
# Importantly accessing this website and downloading from it too many times will lead to you getting suspended for 2 hours.
def TLE_parser_from_web():
    
    #Celestrack URL for TLE on all actively tracked satellites should incorporate methods to update TLE collection after a
    #number of days to ensure accurate data to compare with ROO images
    url = "https://celestrak.org/NORAD/elements/gp.php?GROUP=active&FORMAT=tle"
    
    #From the webpage, writing a txt file of all TLE data
    try:
        tle_page = urllib.request.urlopen(url).read().decode()
        with open('tle_data.txt', 'wb') as tle_file:
            tle_file.write(tle_page.encode())
            tle_file.close
    
    except urlerror as e:
       print (e)
       