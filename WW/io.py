import geopandas as gpd
import xarray as xr
import rioxarray as rxr

rain_nc = 'data'
temp_fname = 'Tair_WFDE5_CRU_dly_v1.0.nc' 

xds = xr.open_dataset(
    "3B-DAY.MS.MRG.3IMERG.20170216-S000000-E235959.V06.nc4",)

