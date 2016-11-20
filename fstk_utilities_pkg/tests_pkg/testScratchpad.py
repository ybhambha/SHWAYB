# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 08:05:22 2016

@author: yashwantbhambhani
"""
#Launching iPython
#If experiencing issues press Ctrl (the control key and not command key on your
#MAC) and D at the same time to exit and then type ipython notebook
#http://python.6.x6.nabble.com/IPython-User-Problem-Running-IPython-Notebook-td4996835.html

import os
import sys
import pandas as pd
import numpy as np

sys.path.append(os.path.abspath('/Users/yashwantbhambhani/Documents/SHWAYB/FSTK'))

#EXAMPLE 1: Inheritence
#from fstk_utilities_pkg.scratchpad.inheritence import *
#
#obj_child = Child('XYZ')
#
#print obj_child.getBase()
 

#EXAMPLE 2: DataFrame Merging
#https://pythonprogramming.net/concatenate-append-data-analysis-python-pandas-tutorial/
#
#df2 = pd.DataFrame({'HPI':[80,85,88,85],
#                    'Int_rate':[2, 3, 2, 2],
#                    'US_GDP_Thousands':[50, 55, 65, 55]},
#                   index = [2005, 2006, 2007, 2008])
#
#df3 = pd.DataFrame({'HPI':[80,85,88,85],
#                    'Int_rate':[2, 3, 2, 2],
#                    'Low_tier_HPI':[50, 52, 50, 53]},
#                   index = [2001, 2002, 2003, 2004])
#                   
##Notice there are two major changes between these. df1 and df3 have the 
##same index, but they have some different columns. df2 and df3 have 
##different indexes and some differing columns. With concatenation, 
##we can talk about various methods of bringing these together. 
##Let's try a simple concatenation:
#
#concat = pd.concat([df1,df2])
#print(concat)
#
##Easy enough. The major difference between these was merely a 
##continuation of the index, but they shared the same columns. Now they have 
##become a single dataframe. In our case, however, we're curious about 
##adding columns, not rows. What happens when we combine some shared and 
##some new:
#
#concat = pd.concat([df1,df2,df3])
#print(concat)
#
##Not bad, we have some NaN (not a number), because this data didn't exist 
##for that index, but all of our data is indeed here.
##
##Those are the basics of concatenation, next up, let's cover appending. 
##Appending is like the first example of concatenation, only a bit more 
##forceful in that the dataframe will simply be appended to, adding to rows. 
##Let's show an example of how it usually works, but also show where it 
##could possibly go wrong:
#
#df4 = df1.append(df2)
#print(df4)
#
##That's what we expect with an append. In most cases, you are going to do 
##something like this, as if you're inserting a new row in a database. 
##Dataframes were not really made to be appended efficiently, they are meant 
##moreso to be manipulated based on their starting data, but you can append 
##if you need to. What happens when we append data with the same index? 
#
#df4 = df1.append(df3)
#print(df4)
#
##Well, that's unfortunate. Some people ask why both concatenation and append 
##exist. That's why. It's far more efficient here to combine these 
##dataframes since the columns shared contain the same data and same index. 
##One more example is to append possibly a series. You're more likely to be 
##appending a series than whole dataframes given the nature of append. We 
##have not spoken about series to this point. A series is basically a 
##single-columned dataframe. A series does have an index, but, if you 
##convert it to a list, it will be just those values. Whenever we say 
##something like df['column'], the return is a series.
#
#s = pd.Series([80,2,50], index=['HPI','Int_rate','US_GDP_Thousands'])
#df4 = df1.append(s, ignore_index=True)
#print(df4)
#
##We have to ignore the index when appending a series, because that is the 
##law, unless the series has a name.

#EXAMPLE 3: how-to-get-a-value-from-a-cell-of-a-data-frame
#    
#
#
#If you have a DataFrame with only one row, then access the first (only) row as a Series using iloc, and then the value using the column name:
#
#In [3]: sub_df
#Out[3]:
#          A         B
#2 -0.133653 -0.030854
#
#In [4]: sub_df.iloc[0]
#Out[4]:
#A   -0.133653
#B   -0.030854
#Name: 2, dtype: float64
#
#In [5]: sub_df.iloc[0]['A']
#Out[5]: -0.13365288513107493

#EXAMPLE 4: Creating an empty dataframe
#columns = ['risk_factor', 'risk_factor_sens']
##index = np.arange(103) # array of numbers for the number of samples
#df = pd.DataFrame(columns=['risk_factor', 'risk_factor_sens'])
#
##myarray = np.random.random((10,3))
##for val, item in enumerate(myarray):
##    df.ix[val] = item
#
#mydata = [{'risk_factor' : 'index1', 'risk_factor_sens': 75},
#          {'risk_factor' : 'index2', 'risk_factor_sens': 22},]
#df = pd.DataFrame(mydata)


#EXAMPLE 5: Setting Correlation dataframe
#import pandas.io.data as web
#import matplotlib.pyplot as plt
##%matplotlib inline
#
##symbols = ['AAPL', 'MSFT', 'YHOO', 'DB', 'GLD']
#symbols = ['AAPL']
#noa = len(symbols)
#
#data = pd.DataFrame()
#
#for sym in symbols:
#    data[sym] = web.DataReader(sym, data_source='yahoo', end='2014-09-12')['Adj Close']
#    data.columns = symbols
#    (data/data.ix[0]*100).plot(figsize=(8,5))
#    rets = np.log(data/data.shift(1))
#    rets.mean() * 252
#    rets.cov() * 252

#EXAMPLE 6: Converting Dataframe to list of unique values
#lst_portfolio_all_risk_factors = pd.unique(df_portfolio_all_risk_factors\
#                                            ['risk_factor'].values.ravel())

from fstk_utilities_pkg.data_access_utilities.data_access_util import *

obj_yahoo = yahoo()
stock_instrument_id = 'NOK'
start_date = '2000-12-29'
end_date = '2006-04-20'

stock_price_data = obj_yahoo.getHistoricalStockPriceData(stock_instrument_id, \
                                                        start_date, end_date)
