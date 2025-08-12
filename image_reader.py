from PIL import Image
from PIL.ExifTags import TAGS
from astropy.io import fits
import datetime
import numpy as np

def jpg_image_reader():

    metadata_value_dict = {}

    jpg_path = "img.jpg"
    image = Image.open(jpg_path)

    image_metadata = image.getexif()

    for tagid in image_metadata:

        tagname = TAGS.get(tagid, tagid)

        value = image_metadata.get(tagid)

        metadata_value_dict[tagname] = value

    print (metadata_value_dict)

    #source: https://www.geeksforgeeks.org/python/how-to-extract-image-metadata-in-python/

def fits_image_reader():
    fits_image_path = "00065184_GPS_BIIRM-1__PRN_17__#28874U_5.000secs_Light.fit"
    with fits.open(fits_image_path) as hdul:

        header = hdul[0].header

        image_time_string_type = header.get("DATE-OBS")
        image_RA = (header.get("OBJCTRA"))
        image_DEC = (header.get("OBJCTDEC"))

        image_RA = image_RA.split()
        image_DEC = image_DEC.split()
        image_RA_1 = float(image_RA[0])
        image_RA_2 = float(image_RA[1])/60
        image_RA_3 = float(image_RA[2])/3600
        image_DEC_1 = float(image_DEC[0])
        image_DEC_2 = float(image_DEC[1])/60
        image_DEC_3 = float(image_DEC[2])/3600
        image_RA = (image_RA_1+image_RA_2+image_RA_3)*(np.pi/180)
        image_DEC = (image_DEC_1+image_DEC_2+image_DEC_3)*(np.pi/180)
        

        image_time = datetime.datetime.strptime(image_time_string_type, "%Y-%m-%dT%H:%M:%S.%f")
        
        return image_time, image_RA, image_DEC
fits_image_reader()

# Source: FITS File Handling (astropy.io.fits) — Astropy v7.1.0. (2025, May 20). Retrieved from https://docs.astropy.org/en/stable/io/fits/index.html
