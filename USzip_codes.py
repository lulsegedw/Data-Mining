from mpl_toolkits.basemap import Basemap
from matplotlib.collections import LineCollection
import matplotlib as mpl
from matplotlib.colors import rgb2hex
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import random as rd

#URL of the dataset to obtain the zip codes
#https://public.opendatasoft.com/explore/dataset/us-zip-code-latitude-and-longitude/export/?location=2,43.32518,-69.78516&basemap=jawg.streets

df = pd.read_csv('us-zip-code-latitude-and-longitude.csv', sep=';')

#Remove the zip code of Alaska (AK) and Hawak (HI)
df.drop(df[df['State'] == 'AK'].index, inplace=True)
df.drop(df[df['State'] == 'HI'].index, inplace=True)


#United States Map bounding box
map = Basemap(llcrnrlon = -125, 
            llcrnrlat = 23,
            urcrnrlon = -66,
            urcrnrlat = 50,
            projection ='mill',
            resolution = 'c')

map.drawcountries()
map.drawcoastlines()

for str_point in df.geopoint:
   point = str_point.split(",")
   #convert the longitude and latitude to image coordinate
   x, y = map(float(point[1]), float(point[0]))
   rgb = [rd.random(), rd.random(), rd.random()] # generate a random color to each zip code location
   map.plot(x, y, marker='s',color=rgb)

plt.show()
