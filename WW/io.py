import geopandas as gpd
import rioxarray as rxr
import matplotlib.pylab as plt
from shapely.geometry import mapping


temp_max_b = 'data/temp_max/Maxtemp_MaxT_2011.GRD'
shp_file = 'data/shapefiles/hydrobasin6_Bangalore_clip_HYBAS_ID_4061139430.0.shp'

xds = rxr.open_rasterio(
    "data/temp_max/Maxtemp_MaxT_2011.nc",
    masked=True,
)
xds.rio.set_crs(4326)
xds[0].plot()
plt.savefig('plots/temp.png')
plt.close()


geodf = gpd.read_file(shp_file)
print(geodf.crs)
geodf.plot()
plt.savefig('plots/shp.png')
plt.close()

clipped = xds.rio.clip(geodf.geometry.apply(mapping), geodf.crs)

clipped.plot()
plt.savefig('plots/clip.png')
plt.close()

