#!/usr/bin/env python
# coding: utf-8

# Designing a NN comes in two parts:
# 1. Data analysis- organise and process the data into the correct requirements of the input of the NN;
# 2. Training- use data to improve performance of NN.
# 
# Here, we (first) analyse the data.

# In[10]:


# Importing data analytic libraries
import pandas as pd
from astropy.table import Table # Astropy works with .fits files
import matplotlib.pyplot as plt


# Process the data using pandas.
# 1. Read the input table with the appropriate format (i.e. fits). Note; this does not cast it as a DataFrame or Series.
# 2. Form a list of the column names of the table.
# 3. Construct a pandas DataFrame column-wise using the column names and the object of each column from the input table.

# In[11]:


class DataAnalysis:
    def __init__(self, dataURL):
        # Processing the data
        gaia = Table.read(dataURL, format="fits")
        names = [name for name in gaia.colnames if len(gaia[name].shape) <= 1]
        # Flattening done here
        self.gaia = gaia[names].to_pandas()

    def getData(self, num):
        return self.gaia[0:num]

    def numRow(self):
        return 30
    
    def numCol(self):
        return len(pd.DataFrame(self.gaia, index=None).axes[1])
    
    # Print data
    def printTable(self):
        print(self.gaia)

    def printPlot(self):
        gaia = self.gaia
        # Plot data
        # Proper Motion + Radial Velocity
        plt.scatter(gaia.pmdec, gaia.pmra, marker='x', linewidths=2, c=gaia.radial_velocity, cmap=plt.cm.inferno, s=1)
        # Create Labels
        plt.xlabel('Proper Motion Declination')
        plt.ylabel('Proper Motion Right Ascension')
        cbar = plt.colorbar()
        cbar.set_label('Radial Velocity')
        plt.title("Motion of Gaia Stars")


# In[14]:


# Show data
# analysis = DataAnalysis("data/star_data.fits")
# analysis.printTable()
# analysis.printPlot()


# Convert to `.py` after `cd` into `src` via: `jupyter nbconvert --to script 'DataAnalysis.ipynb`
