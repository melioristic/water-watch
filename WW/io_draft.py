from WW.cfg import catch_lon_lat
from WW.misc import lat_lon_to_index
from netCDF4 import Dataset
import pandas as pd

def read_temp(var, catchment = 'catch_1'):
    lon, lat = catch_lon_lat[catchment]
    lat_index, lon_index = lat_lon_to_index(lat, lon)
    
    ext = '.nc'
    if var == 'min':
        fname_start = 'data/temp_min/Mintemp_MinT_'
    elif var == 'max':
        fname_start = 'data/temp_max/Maxtemp_MaxT_'

    data = []
    for year in range(2011,2021):
        fname = fname_start + str(year) + ext
        temp_data = Dataset(fname, 'r')
        data.extend(temp_data['t'][:, lat_index, lon_index][:])

    return data

def read_csv(fname = 'data/met_v1_0.csv'):

    return pd.read_csv(fname)