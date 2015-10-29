import os
import json
import numpy as np

SAMPLES = 1201 # For SRTM3, use 3601 for SRTM1


def get_elevation(lat, lon):
    file = get_file_name(lat, lon)
    if file:
        return read_elevation_from_file(file, lat, lon)
    # Treat it as data void as in SRTM documentation
    return -32768


def read_elevation_from_file(file, lat, lon):
    with open(file) as hgt_data:
        # HGT is 16bit signed integer - big endian
        elevations = np.fromfile(hgt_data, np.dtype('>i2'), SAMPLES*SAMPLES)
                                .reshape((SAMPLES, SAMPLES))
        
        lat_row = round((lat - int(lat))* 1200, 0)
        lon_row = round((lon - int(lon))* 1200, 0)
        
        return elevations[1200-lat_row, lon_row].astype(int)

def get_file_name(lat, lon):
    file = "N%(lat)dE0%(lon)d.hgt" % {'lat':lat, 'lon':lon}
    if os.path.isfile(file):
        return file
    else:
        return None

        
        


