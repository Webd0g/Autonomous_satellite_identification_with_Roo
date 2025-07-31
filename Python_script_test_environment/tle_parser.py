# Importing urllib fucntions so that we can extract information from the web
import urllib.request
import urllib.error as urlerror
# We now have a function that pulls the required info from celestrack and writes it as a txt file
# Importantly accessing this website and downloading from it too many times will lead to you getting suspended for 2 hours.
def TLE_parser_from_web():
    url = "https://celestrak.org/NORAD/elements/gp.php?GROUP=active&FORMAT=tle"
    try:
        tle_page = urllib.request.urlopen(url).read().decode()
        tle_file = open('tle_data.txt', 'w')
        tle_file.write(tle_page)
        tle_file.close
    except urlerror as e:
        print (e)

    
         
