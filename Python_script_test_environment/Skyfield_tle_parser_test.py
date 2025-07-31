from skyfield.api import load
max_days = 3
name = 'satellite_data.txt'
base = 'https://celestrak.org/NORAD/elements/gp.php'
url = base + '?GROUP=active&FORMAT=tle'
if not load.exists(name) or load.days_old(name) >= max_days:
    load.download(url, filename=name)