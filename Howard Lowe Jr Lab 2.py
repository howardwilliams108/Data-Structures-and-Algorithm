import sys
import random
from bridges.bridges import * # this will import the main BRIDGES tools.
import pandas as pd # using w3schools, this will store earthquake records in the table
from bridges.data_src_dependent.data_source import *
import matplotlib.pyplot as plt # imports the matplotlib in order to make the graphs

bridges = Bridges(3, "howardwilliams108", "1628069107419") # login to BRIDGES account


earthquake = get_earthquake_usgs_data(100) # retrieving 100 earthquake records from USGS database
                                                 # including time, magnitude time, location and geographic coordinates
# what is happening is that eact earthquake record will process once so it will have the time complexity of O(n)

data = []

for earth in earthquake: # this is a for loop, looping through every earthquake record so the time complexity used is O(n)
  data.append({"magnitude": earth.magnitude, "time": earth.time, "location": earth.location, "latitude": earth.latit, "longitude": earth.longit})

dataf = pd.DataFrame(data) # creating dataframe - turning list into table for sorting and graphing

strongest = dataf.sort_values(by= "magnitude", ascending= False) # this will sort magnitude in descending order i.e. strongest first; time complexity used was O(n log n)
recent = dataf.sort_values(by= "time", ascending= False) # this will sort time in descending order i.e. most recent first
#This will print the top 10 strongest and recent earthquakes, along with the most recent and strongest one.
print("The Top 10 strongest earthquakes include: ")
print(strongest[["magnitude", "location", "time"]].head(10))
print("The Top 10 most recent earthquakes include: ")
print(recent[["time", "location", "magnitude"]].head(10))

print("\nThe most recent earthquake is: ")
print(recent[["time", "location", "magnitude"]].head(1))

print("\nThe strongest earthquake is: ")
print(strongest[["magnitude", "location", "time"]].head(1))

#plotting the scatter plot now, O(n) was used as one point was plotted for each earthquake
plt.figure(figsize = (13, 8))
plt.scatter(dataf["longitude"], dataf["latitude"], c=dataf["magnitude"], cmap = "Greys")

plt.colorbar(label = "Magnitude") # this will show what colors mean
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.title("Earthquake Geo Locations")
plt.show() #this will show the scatterplot

#plotting the bar chart
#Time complexity used is O(n)
bins = [4, 5, 6, 7, 8, 9, 10]
labels = ["4.0-5.0", "5.0-6.0", "6.0-7.0", "7.0-8.0", "8.0-9.0", "9.0 - 10.0"] #each magnitude for earthquakes would be examined once and placed into category
dataf["magnitude_bin"] = pd.cut(dataf["magnitude"], bins=bins, labels=labels)
magnitude_counts = dataf["magnitude_bin"].value_counts().sort_index() #will count earthquakes in each range

plt.figure(figsize= (8,5))
magnitude_counts.plot(kind="bar")
plt.xlabel("Magnitude")
plt.ylabel("Number of Earthquakes Occurred")
plt.title("Earthquake Magnitude Geo Distribution")
plt.show() # this will show the bar chart
