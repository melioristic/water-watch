from WW.io import read_met, read_reservoir

met = read_met()
res = read_reservoir()

#### Slight preprocess, just see that the dates in both the coloumns match 
print(res)