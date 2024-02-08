import sys
import time
import pandas

inputfile='weather_data.csv'
outputfile='preprocessed.csv'

data=pandas.read_csv(inputfile)

#Your code here
#print(data.shape)
data.drop("utc_timestamp", axis=1, inplace= True )
data.dropna(inplace = True)
#print(data.shape)
data.to_csv(outputfile)
