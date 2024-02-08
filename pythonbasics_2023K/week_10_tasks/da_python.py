import numpy as np
import pandas as pd
import pandas.io.json as json_normalize 
import matplotlib.pyplot as plt
from collections import Counter
#import seaborn as sns
import os
import os.path as path
import json


file_text = "yritys_data.json"

path = path.join(path.dirname(path.realpath(__file__)), file_text)

with open(path) as f:
    data_json = json.load(f)

dataOYJ = pd.json_normalize(
    data_json, 
    record_path =['results'],
    max_level=0
)

dataOYJ.drop(["detailsUri", "bisDetailsUri","companyForm"], axis = 1, inplace = True)

list_length = len(dataOYJ.index)

year_list = []
#name_list = []
print(list_length)
for rows in range(list_length):
    temp = dataOYJ._get_value(rows,"registrationDate")
    temp = temp[0] + temp[1] + temp[2] + temp[3]
    year_list.append(temp)
    #temp = dataOYJ._get_value(rows,"name")
    #name_list.append(temp)

counts = dict(Counter(year_list))
chart_values = {key:value for key, value in counts.items()}

x = chart_values.keys()
y = chart_values.values()
print(y)
plt.plot( x , y )
plt.title('OYJ companies registered by year')
plt.ylabel('amount')
plt.xlabel('year')
plt.axis([min(x), max(x), 0, 6])
plt.legend(['companies value', 'test'], loc='upper left')
plt.show()
plt.clf()

#print(chart_values)