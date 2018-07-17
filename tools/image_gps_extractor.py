#derived from https://gist.github.com/moshekaplan/5330395
#Delin Li delin.bio@gmail.com July 17, 2018

import argparse
import re
import sys
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

#maker sure the python version >=3.0
version=(3,0)
cur_version=sys.version_info
if(cur_version <version):
    sys.exit("Require python 3.0+, but yours is "+ sys.version[:3]+"\n")

# get arguments
parser=argparse.ArgumentParser()
parser.add_argument("-f","--file",help="figure file name",type=str,required=True)

args=vars(parser.parse_args())

def get_exif_data(image):
    """Returns a dictionary from the exif data of an PIL Image item. Also converts the GPS Tags"""
    exif_data = {}
    info = getattr(image, '_getexif', lambda: None)()
    if info:
        for tag, value in info.items():
            decoded = TAGS.get(tag, tag)
            if decoded == "GPSInfo":
                gps_data = {}
                for t in value:
                    sub_decoded = GPSTAGS.get(t, t)
                    gps_data[sub_decoded] = value[t]
                exif_data[decoded] = gps_data
            else:
                exif_data[decoded] = value
    return exif_data

def _get_if_exist(data, key):
    if key in data:
        return data[key]
    return None


def _convert_to_degress(value):
    """Helper function to convert the GPS coordinates stored in the EXIF to degress in float format"""
    deg_num, deg_denom = value[0]
    d = float(deg_num) / float(deg_denom)

    min_num, min_denom = value[1]
    m = float(min_num) / float(min_denom)

    sec_num, sec_denom = value[2]
    s = float(sec_num) / float(sec_denom)

    return d + (m / 60.0) + (s / 3600.0)


def get_lat_lon(exif_data):
    """Returns the latitude and longitude, if available, from the provided exif_data (obtained through get_exif_data above)"""
    lat = None
    lon = None

    if "GPSInfo" in exif_data:
        gps_info = exif_data["GPSInfo"]

        gps_latitude = gps_info.get("GPSLatitude")
        gps_latitude_ref = gps_info.get('GPSLatitudeRef')
        gps_longitude = gps_info.get('GPSLongitude')
        gps_longitude_ref = gps_info.get('GPSLongitudeRef')

        if gps_latitude and gps_latitude_ref and gps_longitude and gps_longitude_ref:
            lat = _convert_to_degress(gps_latitude)
            if gps_latitude_ref != "N":
                lat *= -1

            lon = _convert_to_degress(gps_longitude)
            if gps_longitude_ref != "E":
                lon *= -1

    return lat, lon

if __name__ == "__main__":
    image =  Image.open(args["file"])
    exif_data = get_exif_data(image)
    lat,lon=get_lat_lon(exif_data)
    print(re.sub(r'.*/','',args["file"]),lat,lon)

