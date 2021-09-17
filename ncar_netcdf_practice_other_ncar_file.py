# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 23:37:14 2021

@author: Rubix
"""
'''The Data I'm using I got from ncar. Here is the link to it if you're curious: https://www.unidata.ucar.edu/software/netcdf/examples/files.html
I downloadedthe first one on the page. The goal is to make a contour plot of any of those variables. Mainly just for practice
Since I know this stuff will be useful later on in grad school/professional life'''
# %%
'''Importing all the necessary libraries'''
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import numpy as np
import netCDF4 as nc
import matplotlib.pyplot as plt
import xarray as xr
# %%
df = xr.open_dataset('K:/Codes/sresa1b_ncar_ccsm3-example.nc') #opening the file with xarray to see
#what kind of stiff I'm dealing with. Such as 2d or 3d
print(df) #printing df to see what's inside
print('--------------------------------------------------------------------') #this is for splitting it up so I know what print(df)
#did and what print(df.info()) will do. 
print(df.info()) #seeing what's inside it and see what the variables are called and their units. 
# %%
'''Creating the figure'''
fig = plt.figure(figsize = (8, 8)) #creating the figure using matplotlib
ax = plt.subplot(projection = ccrs.PlateCarree()) #creating a subplot to plot in, and defining the projection
ax.add_feature(cfeature.COASTLINE.with_scale('10m'), linewidth = 1) #adding coastlines to the map 
ax.add_feature(cfeature.RIVERS) #adding rivers to the map
ax.add_feature(cfeature.STATES) #adding the states to the map
ax.add_feature(cfeature.BORDERS) #adding other borders to the map
# %%
'''Creating the variables'''
lat = df.variables['lat'][:] #defining latitude
lon = df.variables['lon'][:] #defining longitude
plev = df.variables['plev'][:] #pressure levels in Pa. Air pressure. axis z. Looks like I can say which pressure level I want.
time = df.variables['time'] #defining time
precip = df.variables['pr'][:] #precipitation flux. Units kg m-2 s-1
tas = df.variables['tas'][:] #air temperature in K. Needs a height coordinate
ua = df.variables['ua'][:] #eastward wind in m/s
lon, lat = np.meshgrid(lon, lat) #trying to make lon and lat a 2d array from 1d, and making them the same size
# %%
tas = tas - 273.15 #converting tas from kelvin to celcius
heights_500 = 100/plev[5] #trying to set the data to 500mb, not sure this is useful though
FH = 0 #creating a forecast hour since I still don't know how to go through different times yet
# %%
''' Creating the contours. This is where I am getting stuck. At this point I am willing to plot anything on this, such as tas, precip
or ua, but I can't seem to get any of them to work. There are also a few other variables and if you see anyway to plot those,
that would also be useful so I can see how that was done'''
cf = ax.contourf(lat, lon, precip[0, :, :], cmap=plt.cm.RdBu_r, transform = ccrs.PlateCarree()) #Attempting to make precip contour lines
# but it does not seem to work. I've tried doing tas in there as well but It doesn't seem to work. I've got a feeling it's something
#simple like the arrays are not meant to be plotted like this or something. 
colorbar = fig.colorbar(cf, orientation = 'horizontal', aspect = 70, pad = 0.05, extendrect='True')
#once the plot is made, this colorbar should show up and make the graph much easier to read and understand
plt.show() #plotting the figure