from __future__ import print_function
import os
import numpy as np

SRTM_DICT = {'SRTM1': 3601, 'SRTM3': 1201}

# Get the type of SRTM files or use SRTM3 by default
SRTM_TYPE = os.getenv('SRTM_TYPE', 'SRTM3')
SAMPLES = SRTM_DICT[SRTM_TYPE]

# put uncompressed hgt files in HGT_DIR, defaults to 'hgt'
HGTDIR = os.getenv('HGT_DIR', 'hgt')


def get_elevation(lat, lon):
    hgt_file = get_file_name(lat, lon)
    if hgt_file:
        return read_elevation_from_file(hgt_file, lat, lon)
    # Treat it as data void as in SRTM documentation
    # if file is absent
    return -32768


def read_elevation_from_file(hgt_file, lat, lon):
    with open(hgt_file, 'rb') as hgt_data:
        # HGT is 16bit signed integer(i2) - big endian(>)
        elevations = np.fromfile(
            hgt_data,  # binary data
            np.dtype('>i2'),  # data type
            SAMPLES * SAMPLES  # length
        ).reshape((SAMPLES, SAMPLES))

        lat_row = int(round((lat - int(lat)) * (SAMPLES - 1), 0))
        lon_row = int(round((lon - int(lon)) * (SAMPLES - 1), 0))

        return elevations[SAMPLES - 1 - lat_row, lon_row].astype(int)


def get_file_name(lat, lon):
    """
    Returns filename such as N27E086.hgt, concatenated
    with HGTDIR where these 'hgt' files are kept
    """
    if lat >= 0:
        ns = 'N'
    elif lat < 0:
        ns = 'S'

    if lon >= 0:
        ew = 'E'
    elif lon < 0:
        ew = 'W'

    hgt_file = "%(ns)s%(lat)02d%(ew)s%(lon)03d.hgt" % \
               {'lat': abs(lat), 'lon': abs(lon), 'ns': ns, 'ew': ew}
    hgt_file_path = os.path.join(HGTDIR, hgt_file)
    if os.path.isfile(hgt_file_path):
        return hgt_file_path
    else:
        return None


if __name__ == '__main__':
    # Mt. Everest
    print('Mt. Everest: %d' % get_elevation(27.988056, 86.925278))
    # Kanchanjunga
    print('Kanchanjunga: %d' % get_elevation(27.7025, 88.146667))
