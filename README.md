# srtm-python 
[![Build Status](https://travis-ci.org/aatishnn/srtm-python.svg?branch=master)](https://travis-ci.org/aatishnn/srtm-python)

A python program that reads SRTM1 and SRTM3 Digital Elevation Model files.

Read on how this works: [https://librenepal.com/article/reading-srtm-data-with-python/](https://librenepal.com/article/reading-srtm-data-with-python/)

# Usage
1. Put uncompressed *.hgt files on hgt/ directory or redefine the location of this
directory with `HGT_DIR` environment variable.
2. By default, the code will assume SRTM3 as the data format. You can also
change it with `SRTM_TYPE` environment variable.
3. Enjoy
```python
from srtm import get_elevation
print('Mt. Everest's Elevation: %d' % get_elevation(27.988056, 86.925278))
```
# Contributors
- [@blebo](https://github.com/blebo)
- [@hilsonshrestha](https://github.com/hilsonshrestha)
- [@gamb](https://github.com/gamb)
- [@23pointsNorth](https://github.com/23pointsNorth)
