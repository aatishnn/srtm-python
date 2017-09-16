import unittest
from srtm import get_elevation, get_file_name


'''
These elevation values were taken using gdallocationinfo command which is
a part of gdal-bin package. You can install it in Ubuntu (or derivatives)
using:
    sudo apt-get install gdal-bin
'''

TEST_DATA = [
    {
        'name': 'Mt. Everest',
        'lat': 27.988056,
        'lon': 86.925278,
        'filename': 'hgt/N27E086.hgt',
        # gdallocationinfo N27E086.hgt -wgs84 86.925278 27.988056
        'alt': 8840
    },
    {
        'name': 'Mt. Kanchanjunga',
        'lat': 27.7025,
        'lon': 88.146667,
        'filename': 'hgt/N27E088.hgt',
        # gdallocationinfo N27E088.hgt -wgs84 88.146667 27.7025
        'alt': 8464
    }
]


class TestSRTMMethods(unittest.TestCase):

    def test_get_elevation(self):
        for mountain in TEST_DATA:
            elevation = get_elevation(mountain['lat'], mountain['lon'])
            self.assertEquals(elevation, mountain['alt'])

    def test_get_file_name(self):
        for mountain in TEST_DATA:
            filename = get_file_name(mountain['lat'], mountain['lon'])
            self.assertEquals(filename, mountain['filename'])


if __name__ == '__main__':
    unittest.main()
