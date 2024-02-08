import pandas
from scipy import stats
import numpy as np
from sklearn import preprocessing

inputfile='time_series.csv'
trainfile='train.csv'
testfile='test.csv'

data=pandas.read_csv(inputfile)

#Your code here

#print(data.shape)


data.drop(data.index[data["region"] != "DE"] , axis=0, inplace=True)
data.drop(data.index[data["variable"] != "wind"] , axis=0, inplace=True)
data.drop(data.index[data["attribute"] != "generation_actual"] , axis=0, inplace=True)
# other option data.loc[data["region"] == "DE" & ... ]

data.drop(["region", "variable", "attribute"], axis = 1, inplace=True)
data.dropna(inplace = True)

#z score
z_threshold = 4.0
z = np.abs(stats.zscore(data["data"]))
#outlier = (z >= z_threshold)
filtered = (z < z_threshold)
data = data[filtered]

data[["data"]] = preprocessing.MinMaxScaler().fit_transform(data[["data"]])

train_fraction = 0.7

traindata = data.sample(frac=train_fraction, random_state = 200)

testdata = data.drop(traindata.index)

#print(scaler)
#print(data.shape)


#Save train data
print("Save train data")
traindata.to_csv(trainfile)

#Save test data
print("Save test data")
testdata.to_csv(testfile)

