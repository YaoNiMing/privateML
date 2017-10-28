# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 10:44:04 2016

@author: Rohan
"""

nf = pd.read_csv('/Users/Rohan/Desktop/Code/pchall.csv')

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
nf.head()
nf['Date'] = pd.to_datetime(nf["ReleaseDate"])
nf['DomesticTotalGross'] = nf['DomesticTotalGross'].astype(float)
nf['Runtime'] = nf['Runtime'].astype(float)

nf = nf.sort_values('Date')
plt.plot_date(x=nf["Date"], y=nf["DomesticTotalGross"],fmt="r-") 
plt.title("Timeseries")
plt.ylabel("Total")
plt.grid(True)
plt.show()


nf = nf.sort_values('Runtime')
plt.plot(nf["Runtime"],nf["DomesticTotalGross"])
plt.title("Runtime vs Gross")
plt.ylabel("Total")
plt.xlabel("Runtime")
plt.grid(True)
plt.show()

##Group your data by Rating and find the average runtime 
#and domestic total gross at each level of Rating.


nf.groupby(["Rating"])["Runtime", "DomesticTotalGross"].mean(). plot(subplots=True)

"""     
          Runtime  DomesticTotalGross
Rating                                
G       107.000000        2.684928e+08
PG       99.933333        1.311357e+08
PG-13   117.510638        1.114498e+08
R       110.729730        6.989243e+07

"""

#Make one figure with (N=the number of MPAA ratings there are) 
#subplots, and in each plot the release date vs the domestic total gross.



pd.pivot_table(nf.reset_index(),
               index='Date', columns='Rating', values='DomesticTotalGross'
              ).plot(subplots=True, linestyle = '', marker = 'o')



nf.groupby(["Director"])["DomesticTotalGross"].mean().sort_values()
#Francis Lawrence

#Bin your dataset into months and make a bar graph of the mean domestic 
#total gross by month.  Error bars will represent the standard error of the mean.

#Title of graph should include:  Mean Domestic Total Gross by Month in 2013

#Topic for consideration:  what is the correct 
#formula for the standard error of the mean?  
#Examine the error bars and see if they are "reasonable."


n = nf.groupby(pd.Grouper(key='Date', freq='M'))["DomesticTotalGross"].mean()
m = nf.groupby(pd.Grouper(key='Date', freq='M'))["DomesticTotalGross"].std()
m

no = pd.DataFrame({'D':n.index, 'gross':n.values})
mo = pd.DataFrame({'D':m.index, 'err':m.values})

no.head()
l1  = [1,2,3,4,5,6,7,8,9,10,11,12]
no["month"] = l1



plt.title('Mean Domestic Total Gross by Month in 2013')
 
plt.show()

#######
fig, ax = plt.subplots(1,1, figsize=(5,10))
ax.set_title('Mean Domestic Total Gross by Month in 2013')
sns.barplot(x=no['month'].sort_values(), y=no['gross'], errwidth = 20, errcolor = "r")
plt.errorbar(no.month, no.gross, mo.err, linestyle='None', marker='^')
ax.set_xlabel('Month')
ax.set_ylabel('Total')




