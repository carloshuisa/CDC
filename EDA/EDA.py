#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 09:45:07 2021

@author: nicolehanrahan
"""

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

social = pd.read_csv('/Users/nicolehanrahan/Downloads/socialdata.csv')

# Check unique values in each column
n = social.nunique(axis=0)
print(n)

# Unclear what these variables are...
# FID 
# AFFGEOID
# TRACTCE

# Variable definition available, but not intuitive
# STCNTY
# FIPS

# EP_PCI and E_PCI are redundant
# MP_PCI and M_PCI are redundant

# STATE, ST, and ST_ABBR are redundant, only need one
social.STATE.unique()
social.ST.unique()
social.ST_ABBR.unique()

# Min / Max
min = social.min()
max = social.max()
var = social.columns

array1 = np.column_stack((var,min,max))
df1 = pd.DataFrame(data = array1,  
                        columns = ["Variable", "Min",
                                   "Max"])

print(df1)

# Outlier Histogram Test

fig, ax = plt.subplots(figsize=(10,7))
ax.hist(social['E_HU'], bins = [0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000])

plt.show()



