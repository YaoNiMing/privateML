
# coding: utf-8

# In[48]:

# import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
import matplotlib as matplotlib
#import dateutil.parser

from IPython.display import Image

from IPython.display import Image

# enables inline plots, without it plots don't show up in the notebook
# get_ipython().magic(u'matplotlib inline')

# various options in pandas
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 25)
pd.set_option('display.precision', 3)


# 1.: Download a couple of MTA data sets and combine them into a data frame

# In[49]:

# downloading a couple of MTA data sets and combining them

df = pd.read_csv('http://web.mta.info/developers/data/nyct/turnstile/turnstile_160917.txt')
dftemp = pd.read_csv('http://web.mta.info/developers/data/nyct/turnstile/turnstile_160910.txt')
df = df.append(dftemp, ignore_index = True)
dftemp = pd.read_csv('http://web.mta.info/developers/data/nyct/turnstile/turnstile_160903.txt')
df = df.append(dftemp, ignore_index = True)

df.to_csv(path_or_buf='turnstile.csv')

# Sort by C/A, Unit, SCP, Station

# df = df.sort_values(["C/A", "UNIT", "SCP", "STATION"])



# # 2.: Turn this into a time series

# # In[50]:

# # Add a column that combines date and time in the datetime format

# df["DATETIME"] = df["DATE"] + " " + df["TIME"] 
# df["DATETIME"] = pd.to_datetime(df.DATETIME, infer_datetime_format=True)


# # In[51]:

# # Get rid of not needed columns

# df = df.drop(['LINENAME', 'DIVISION', 'DESC'], axis = 1)


# # 3.: Reduce number of entries to daily data

# # In[52]:

# # hourly interval

# hourly_interval = df.DATETIME.loc[1] - df.DATETIME.loc[0]
# hourly_interval


# # In[53]:

# # Sort by date and time

# df=df.sort_values(["C/A", "UNIT", "SCP", "STATION", "DATETIME"])
# df


# # In[54]:

# df=df.groupby(["C/A", "UNIT", "SCP", "STATION","DATE"])[["TIME", "ENTRIES"]].max().reset_index()


# # In[55]:

# df["DAILYENTRIES"]=df.ENTRIES.diff()
# df[df.DATE == "08/27/2016"]


# # In[56]:

# df=df[df.DATE > "09/02/2016"]


# # In[57]:

# # In[ ]:

# #lost money per day per closed station 


# # In[58]:

# df.sort_values(by='ENTRIES')


# # # In[65]:

# # df = df.groupby('STATION')['ENTRIES'].mean()


# # df['mean_by_station'] = np.where(df.mean('ENTRIES'))

# # # In[63]:
# matplotlib.pyplot.show()
# # df.sort_values
# fifty9th = df.STATION.str.contains('59 ST')
# df1 = df[fifty9th]
# # In[ ]:
# df1['ENTRIES'].plot

# plt.show()



