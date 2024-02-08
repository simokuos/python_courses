import sys
import time
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

inputfile='in.npy'
outputfile='out.npy'

data=np.load(inputfile)

#Your code here
#print(data.shape)

pca = PCA(22)
pca.fit(data)

packed_data= pca.transform(data)

plt.plot(packed_data, "*" )
plt.show()





#fig = plt.figure(figsize=(18, 8))
#plt.plot(data, "*")
#plt.show()



np.save(outputfile, packed_data)
