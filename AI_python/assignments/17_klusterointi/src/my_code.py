import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score


data = pd.read_csv("painteddata.csv")

#Your code here
#print(data.shape)

n_clusters_array = [i for i in range(2, 10)]
silhouette_avg = []
max_sil_score = 0
max_silscore_index = 0
for count, n_clusters in  enumerate(n_clusters_array):
    kmeans = KMeans(n_clusters=n_clusters, n_init="auto").fit(data)
    kmeans_classID = kmeans.labels_
    sil_score = silhouette_score(data, kmeans_classID)
    if max_sil_score < sil_score: 
        max_sil_score = sil_score
        max_silscore_index = count
    silhouette_avg.append(sil_score)

n_clusters = n_clusters_array[max_silscore_index]

print(n_clusters)
