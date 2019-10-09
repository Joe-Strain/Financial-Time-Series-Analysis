# Tesla Stock performance analysis against Ford and General Motors
# -- Data collected from NYSE --

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()

# import Tesla, Ford, General Motor stock data from 01/01/2012 - 01/01/2017
df_tesla = pd.read_csv('Tesla_Stock.csv',index_col=0)
df_ford = pd.read_csv('Ford_Stock.csv',index_col=0)
df_GM = pd.read_csv('GM_stock.csv',index_col=0)


# Create dataframe of all open prices
df_allopen = pd.concat([df_tesla['Open'],df_ford['Open'],df_GM['Open']],axis=1)
df_allopen.columns = ['Tesla', 'Ford', 'GM']


# Line plot of open prices
df_allopen.plot(title='Open Price')
plt.legend()
plt.show()


# Create dataframe of volume traded 
df_allvolume = pd.concat([df_tesla['Volume'],df_ford['Volume'],df_GM['Volume']],axis=1)
df_allvolume.columns = ['Tesla', 'Ford', 'GM']


# Plot volume traded
df_allvolume.plot(title='Daily Volume Traded',lw=1)
plt.legend()
plt.show()