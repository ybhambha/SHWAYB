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
import math
from fstk_utilities_pkg.portfolio_manager.portfolio import *
from fstk_utilities_pkg.instruments.equity import *
from fstk_utilities_pkg.data_access_utilities.data_access_util import *
from fstk_utilities_pkg.risk_manager.equity_risk import *
from fstk_utilities_pkg.common_utilities.array_util import *

volume = "vol2"
chapter = "chap01"
example = "eg06"

portfolio_name = "port_" + volume + "_" + chapter + "_" + example 
obj_portfolio = portfolio(portfolio_name)

obj_df_risk_factors_data = DataAsDataFrame(DatasetTypeList.DATAFRAME)
obj_df_equity_instruments_data = DataAsDataFrame(DatasetTypeList.DATAFRAME)
obj_df_portfolio_assets_betas_data = DataAsDataFrame(DatasetTypeList.DATAFRAME)
obj_df_portfolio_data = DataAsDataFrame(DatasetTypeList.DATAFRAME)

df_risk_factors_data = obj_df_risk_factors_data.getData(\
                                s_volume=volume, s_chapter=chapter,\
                                s_example=example, \
                                s_source_filename="Risk_Factors", \
                                s_source_type="csv", verbose=False)

df_equity_instruments_data = obj_df_equity_instruments_data.getData(\
                                s_volume=volume, s_chapter=chapter,\
                                s_example=example, \
                                s_source_filename="Equity_Instruments", \
                                s_source_type="csv", verbose=False)

df_portfolio_assets_beta_data = obj_df_portfolio_assets_betas_data.getData(\
                                s_volume=volume, s_chapter=chapter,\
                                s_example=example, \
                                s_source_filename="Portfolio_Betas", \
                                s_source_type="csv", verbose=False)                                

df_portfolio_data = obj_df_portfolio_data.getData(\
                                s_volume=volume, s_chapter=chapter,\
                                s_example=example, \
                                s_source_filename="Portfolio", \
                                s_source_type="csv", verbose=False)

##Setting universe of risk factors
#arr_risk_factors = []
#
#for risk_factor in df_risk_factors_data.index:
#    obj_risk_factor = equity_risk_factor(risk_factor,\
#                        df_risk_factors_data.ix[risk_factor]['Asset Class'])    
#    arr_risk_factors.append(obj_risk_factor)
#                                                 
##Setting universe of equity instruments
#arr_equity_instruments = []
#
#for equity_instrument in df_equity_instruments_data.index:
#    obj_equity = equity_valuation_multi(equity_instrument)
#    for risk_factor in arr_risk_factors:
#        if risk_factor.getAssetClass() == risk_factor_asset_class.EQT:
#            obj_equity.addRiskFactor(risk_factor.getRiskFactorName())
#            if (risk_factor.getRiskFactorName() == 'Index1'):
#                obj_equity.setRiskFactorSensValue(risk_factor.getRiskFactorName(),\
#                        df_portfolio_assets_beta_data.ix[equity_instrument]['Beta 1'])
#            elif (risk_factor.getRiskFactorName() == 'Index2'):
#                obj_equity.setRiskFactorSensValue(risk_factor.getRiskFactorName(),\
#                        df_portfolio_assets_beta_data.ix[equity_instrument]['Beta 2'])
#    arr_equity_instruments.append(obj_equity)
#
##Creating a new portfolio
#obj_portfolio = portfolio(portfolio_name)
#
##Adding positions to the portfolio
#for portfolio_item in df_portfolio_data.index:
#    #Get the corresponding equity object from the array of equity objects
#    for equity_obj in arr_equity_instruments:
#        if equity_obj.getIdentifier() == portfolio_item:
#            obj_position = equity_position(equity_obj, position_type.EQT,\
#                                df_portfolio_data.ix[portfolio_item]['Weight'],
#                                df_portfolio_data.ix[portfolio_item]['Weight'])
#            obj_portfolio.addPosition(obj_position)
#
#arr_portfolio_positions = obj_portfolio.getPositions()
#arr_portfolio_positions_betas = obj_portfolio.getPositionsBetas()
#
##Filtering correlations data to get correlation matrix for stocks in the portfolio
###This information should be cached
#obj_db = Db()
#df_all_risk_factors_correlations = \
#                        obj_db.getAllRiskFactorsCorrelations()
#                        
##Retrieve all the correlations for the risk factors of the portfolio
#lst_portfolio_all_risk_factors = obj_portfolio.getAllRiskFactors()
#row_filter = lst_portfolio_all_risk_factors
#column_filter = lst_portfolio_all_risk_factors                        
#df_portfolio_stocks_risk_factors_correlations = \
#            df_all_risk_factors_correlations.ix[row_filter][column_filter]
#lst_portfolio_stocks_risk_factors_correlation = \
#            df_portfolio_stocks_risk_factors_correlations.values.tolist()
#            
##Calculate Variance Covariance Matrix of risk factors
#obj_array_util = array_util()
#lst_equities_risk_factors = obj_portfolio.getAllRiskFactors()
#ser_risk_factors_vol_data = df_risk_factors_data['Volatility']
#df_risk_factors_vol_data = pd.DataFrame(ser_risk_factors_vol_data)
#mat_portfolio_risk_factors_var_covar = obj_array_util.calc_var_covar_matrix(\
#                                obj_portfolio.getAllRiskFactors().tolist(), \
#                                df_risk_factors_vol_data,\
#                                lst_portfolio_stocks_risk_factors_correlation
#                                )
#                                
#obj_portfolio.setPortfolioRiskFactorsVarCovarMatrix(\
#                                mat_portfolio_risk_factors_var_covar)                          
#
#obj_portfolio.calcPortfolioRisk()
#
#print '*************INPUTS**************'
#print '*********************************'
#print ''
#print df_portfolio_data
#print '*********************************'
#print df_portfolio_assets_beta_data
#print '*********************************'
#print df_risk_factors_data
#print ''
#print '************OUTPUTS**************'
#print '*********************************'
#print ''
#print '************Net Betas of stocks in portfolio************'
#print obj_portfolio.getAllRiskFactors()
#print obj_portfolio.getPortfolioBeta()    
#print '********************************************************'
#print '***********Covariance Matrix of risk factors************'
#print mat_portfolio_risk_factors_var_covar
#print '*********Portfolio Variance due to risk factors*********'
#print obj_portfolio.getPortfolioVariance()
#print '*********Portfolio Volatility due to risk factors*********'
#print obj_portfolio.getPortfolioVolatility()

obj_db = Db()
lst_all_risk_factors_correlations = \
                        obj_db.getAllRiskFactorsCorrelations_2()
