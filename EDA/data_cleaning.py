# Load libraries
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns

# Define working directory
os.chdir('C:/Users/james/OneDrive/Desktop/Coding/Jupyter Notebook/cdc_datasets/social science')

# Import original data (csv file)
svi = pd.read_csv('svi.csv')

# Read in data
svi.head()

# Check null values, data type, and unique values in each column
null = svi.isnull().sum().to_frame(name='nulls').T
dtype = svi.dtypes.to_frame(name='dtypes').T
nunique = svi.nunique().to_frame(name='unique').T
pd.concat([null, dtype, nunique], axis=0)

# Filter original dataset by NC
svi_nc = svi.loc[svi['ST_ABBR'] == 'NC']
svi_nc.head()

# Get column names containing missing values -999
svi_nc.columns[svi_nc.isin([-999]).any()]

# Create a data frame with only columns that contain -999
svi_nc_m = svi_nc.loc[:, ['E_PCI', 'M_PCI', 'MP_POV', 'MP_UNEMP', 'EP_PCI', 'MP_PCI', 'MP_NOHSDP',
       'MP_AGE65', 'MP_AGE17', 'MP_DISABL', 'MP_SNGPNT', 'MP_MINRTY',
       'MP_LIMENG', 'MP_MUNIT', 'MP_MOBILE', 'MP_CROWD', 'MP_NOVEH',
       'MP_GROUPQ', 'EPL_PCI', 'SPL_THEME1', 'RPL_THEME1', 'RPL_THEME2',
       'RPL_THEME3', 'RPL_THEME4', 'SPL_THEMES', 'RPL_THEMES', 'F_PCI',
       'F_THEME1', 'F_THEME2', 'F_THEME3', 'F_THEME4', 'F_TOTAL', 'MP_UNINSUR',
       'E_DAYPOP']]
       
# Create a list containing number of missing values in each column
lst_col = []
lst_miss = []

for i in range(len(svi_nc_m.columns)):
    
    col_name = [svi_nc_m.columns[i]]
    num_miss = [len(svi_nc_m[svi_nc_m[svi_nc_m.columns[i]] == -999])]
    
    for col in col_name:
        lst_col.append(col)
        
    for num in num_miss:
        lst_miss.append(num)
        
print(lst_col)
print(lst_miss)

# Create a data frame that contains column name and its number of missing values
df_col = pd.DataFrame(lst_col, columns = ['col_name'])
df_num = pd.DataFrame(lst_miss, columns = ['miss_count'])

df_miss = pd.concat([df_col, df_num], axis = 1, join = 'inner')
df_miss

# Impute missing values in each column
# Continuous variables: impute with the median value of all counties (NOT the median value of each county)
# Categorical variables: impute with 0

col_lst1 = ['E_PCI', 'M_PCI', 'MP_POV', 'MP_UNEMP', 'EP_PCI', 'MP_PCI', 'MP_NOHSDP', 'MP_AGE65', 'MP_AGE17', 
           'MP_DISABL', 'MP_SNGPNT', 'MP_MINRTY','MP_LIMENG', 'MP_MUNIT', 'MP_MOBILE', 'MP_CROWD', 'MP_NOVEH',
           'MP_GROUPQ', 'EPL_PCI', 'SPL_THEME1', 'RPL_THEME1', 'RPL_THEME2', 'RPL_THEME3', 'RPL_THEME4', 
            'SPL_THEMES', 'RPL_THEMES', 'MP_UNINSUR', 'E_DAYPOP']
col_lst2 = ['F_PCI', 'F_THEME1', 'F_THEME2', 'F_THEME3', 'F_THEME4', 'F_TOTAL']


for i in range(len(col_lst1)):
    svi_nc[col_lst1[i]] = svi_nc[col_lst1[i]].replace(-999, svi_nc[col_lst1[i]].median())
    
for j in range(len(col_lst2)):
    svi_nc[col_lst2[j]] = svi_nc[col_lst2[j]].replace(-999, 0)
    
# Check imputation: Outputs should be 0
print(len(svi_nc[svi_nc['E_PCI'] == -999]))
print(len(svi_nc[svi_nc['F_PCI'] == -999]))