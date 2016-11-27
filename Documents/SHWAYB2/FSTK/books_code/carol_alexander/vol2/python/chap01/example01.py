# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 00:25:27 2016

@author: yashwantbhambhani
"""
import numpy
from numpy import *
import pandas as pd
import statsmodels.formula.api as sm
import sys

sys.path.append(os.path.abspath('/Users/yashwantbhambhani/Documents/SHWAYB/FSTK'))

from config.config import *

obj_config = config()
carol_alexander_book_data_path = obj_config.get_carol_alexander_book_data_path()
data_path = carol_alexander_book_data_path + '/vol2/chap01/eg01/'

# Reading the file
dfStockReturns = pd.read_csv(data_path + 'EX_II.1.1.csv', \
                                skiprows=[1], sep=',', index_col=0)

x=dfStockReturns['SPX Rtn'].values
y=dfStockReturns['MSFT Rtn'].values

regression = numpy.polyfit(x, y, 1)
print regression

# Alternative way to get regression results (Using OLS library)

dfStockReturns.head()

Y = dfStockReturns['MSFT Rtn']  # response
X = dfStockReturns['SPX Rtn']  # predictor
#X = sm.add_constant(X)  # Adds a constant term to the predictor

est = sm.OLS(Y, X)
est = est.fit()
print est.summary()