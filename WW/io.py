import geopandas as gpd
import rioxarray as rxr
import matplotlib.pylab as plt

temp_max_b = 'data/temp_max/Maxtemp_MaxT_2011.GRD'

with open(temp_max_b, 'rb') as f:
    print(f.readline().decode()) 



# xds = rxr.open_rasterio(
#     "data/temp_max/Bangalore.shp",
#     masked=True,
# )

# xds.plot()
# plt.savefig('plots/banglore.png')

# temp_fname = 'Tair_WFDE5_CRU_dly_v1.0.nc' 

