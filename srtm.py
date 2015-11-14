import os
import json
import numpy as np

SAMPLES = 1201 # Change this to 3601 for SRTM1
HGTDIR = 'hgt' # All 'hgt' files will be kept here uncompressed

def get_elevation(lon, lat):
    file = get_file_name(lon, lat)
    if file:
        return read_elevation_from_file(file, lon, lat)
    # Treat it as data void as in SRTM documentation
    # if file is absent
    return -32768


def read_elevation_from_file(file, lon, lat):
    with open(file) as hgt_data:
        # HGT is 16bit signed integer(i2) - big endian(>)
        elevations = np.fromfile(hgt_data, np.dtype('>i2'), SAMPLES*SAMPLES)\
                                .reshape((SAMPLES, SAMPLES))
        
        lat_row = round((lat - int(lat))* 1200, 0)
        lon_row = round((lon - int(lon))* 1200, 0)
        
        return elevations[1200-lat_row, lon_row].astype(int)

def get_file_name(lon, lat):
    '''
    Returns filename such as N27E086.hgt, concatenated
    with HGTDIR where these 'hgt' files are kept 
    '''
    file = "N%(lat)02dE%(lon)03d.hgt" % {'lat':lat, 'lon':lon}
    file = os.path.join(HGTDIR, file)
    if os.path.isfile(file):
        return file
    else:
        return None


if __name__ == '__main__':
    # Mt. Everest
    print get_elevation(86.925278, 27.988056)
    # Kanchanjunga
    print get_elevation(88.146667, 27.7025)
        
        


