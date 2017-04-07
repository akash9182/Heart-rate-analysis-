# import csv 

# with open('/home/jarvis/Desktop/SQLITE DATABASE/SOURABHDB/MI_BAND_ACTIVITY_SAMPLE_csv.csv', 'rb') as csvfile:
# 	spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
# 	seconds = 00
# 	minutes = 00
# 	count = 4
# 	time = 0
# 	for row in spamreader:
# 		# if (seconds == 60):
# 		# 	seconds = 0
# 		# 	minutes = minutes + 1
# 		# time = "9:" + str(minutes) + ":" +str(seconds)
# 		# seconds = seconds + 15
# 		row.append(str(time))
# 		print(', '.join(row))
# 		time = time + 1

import os
# import matplotlib as mpl
import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib.cbook as cbook
import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go
py.sign_in('Akash__rana', 'hG77i5HTxFyImhc7ft26')
import datetime

def read_datafile(file_name):
    # the skiprows keyword is for heading, but I don't know if trailing lines
    # can be specified
    data = np.loadtxt(file_name, delimiter=',',skiprows= 0 )
    return data

path = os.getcwd()

# print(path)

akash = pd.read_csv(path + '/AKASHDB/MI_BAND_ACTIVITY_SAMPLE_CSV.csv')

akash.drop(['DEVICE_ID', 'USER_ID','STEPS', 'RAW_KIND', 'RAW_INTENSITY'],1,inplace=True)
akash['HEART_RATE'].replace(to_replace=0,  value = 0,method='ffill')
akash['new_col'] = range(1, len(akash) + 1)

pallavi = pd.read_csv(path +'/PALLAVIDB/MI_BAND_ACTIVITY_SAMPLE_csv.csv')
pallavi.drop(['DEVICE_ID', 'USER_ID','STEPS', 'RAW_KIND', 'RAW_INTENSITY'],1,inplace=True)
pallavi['HEART_RATE'].replace(to_replace=0,value = 0, method='ffill')
pallavi['new_col'] = range(1, len(pallavi) + 1)

sourabh = pd.read_csv(path + '/SOURABHDB/MI_BAND_ACTIVITY_SAMPLE_csv.csv')
sourabh.drop(['DEVICE_ID', 'USER_ID','STEPS', 'RAW_KIND', 'RAW_INTENSITY'],1,inplace=True)
sourabh['HEART_RATE'].replace(to_replace=0,value = 0, method='ffill')
sourabh['new_col'] = range(1, len(sourabh) + 1)

sudip = pd.read_csv(path + '/SUDIPDB/MI_BAND_ACTIVITY_SAMPLE_csv.csv')
sudip.drop(['DEVICE_ID', 'USER_ID','STEPS', 'RAW_KIND', 'RAW_INTENSITY'],1,inplace=True)
sudip['HEART_RATE'].replace(to_replace=0,value = 0, method='ffill')
sudip['new_col'] = range(1, len(sudip) + 1)

# print(akash.keys())
print(sudip)
print(akash.dtypes)
