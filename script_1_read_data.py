from WW import read_temp
import pandas as pd


min_1 = read_temp('min', catchment = 'catch_1')
min_2 = read_temp('min', catchment = 'catch_2')
min_3 = read_temp('min', catchment = 'catch_3')
min_4 = read_temp('min', catchment = 'catch_4')

max_1 = read_temp('max', catchment = 'catch_1')
max_2 = read_temp('max', catchment = 'catch_2')
max_3 = read_temp('max', catchment = 'catch_3')
max_4 = read_temp('max', catchment = 'catch_4')

day = pd.read_csv('data/rainfall/C1_rainfall_new.csv', header = 1).values[:,0]
precip_1 = pd.read_csv('data/rainfall/C1_rainfall_new.csv', header = 1).values[:,1]
precip_2 = pd.read_csv('data/rainfall/C2_rainfall_new.csv', header = 1).values[:,1]
precip_3 = pd.read_csv('data/rainfall/C3_rainfall_new.csv', header = 1).values[:,1]
precip_4 = pd.read_csv('data/rainfall/C4_rainfall_new.csv', header = 1).values[:,1]

data = pd.DataFrame([day, precip_1, precip_2, precip_3, precip_4, min_1, min_2, min_3, min_4, max_1, max_2, max_3, max_4]).T

data.columns = ['day', 'precip_1', 'precip_2', 'precip_3', 'precip_4', 't_min_1',
                't_min_2', 't_min_3', 't_min_4', 't_max_1', 't_max_2', 't_max_3', 't_max_4']

data.to_csv('data/met_v1_0.csv', index=False)  