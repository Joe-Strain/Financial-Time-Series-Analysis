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

maxvolumeford = df_allvolume['Ford'].max()
datemaxvolumeford = df_allvolume['Ford'].idxmax()

print("The largest volume of Ford shares traded in a single day (",maxvolumeford, ") occured on ", datemaxvolumeford)
print("From searching news articles on the web, around this date, the high Ford trading activity appears to be the result of a surprise profit warning, for 2014, issued by the then CFO Bob Shanks.")

# Visual representation of the total amount of money being traded daily, for each stock
# Create new column "Total Traded" for the 3 stocks (Open price * Volume)
df_2tradedtesla = pd.concat([df_tesla, df_tesla["Open"] * df_tesla["Volume"]], axis=1)
df_2tradedtesla.rename(columns={0:"Total Traded"}, inplace=True)

df_2tradedford = pd.concat([df_ford, df_ford["Open"] * df_ford["Volume"]], axis=1)
df_2tradedford.rename(columns={0:"Total Traded"}, inplace=True)

df_2tradedGM = pd.concat([df_GM, df_GM["Open"] * df_GM["Volume"]], axis=1)
df_2tradedGM.rename(columns={0:"Total Traded"}, inplace=True)


# Plot this "Total Traded" against the time index
df_totaltraded = pd.concat([df_2tradedtesla["Total Traded"],df_2tradedford["Total Traded"],df_2tradedGM["Total Traded"]],axis=1)
df_totaltraded.columns = ["Tesla","Ford","GM"]

ax = df_totaltraded.plot(title="Total Value ($) Traded on NYSE",lw=0.8)
ax.set_ylabel('Value Traded ($)')
plt.legend()
plt.show()
