def lat_lon_to_index(lat, lon):
    lat_index  = int(lat - 7)
    lon_index = int(lon - 67)
    return (lat_index, lon_index)