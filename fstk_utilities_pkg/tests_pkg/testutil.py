# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 07:43:26 2016

@author: yashwantbhambhani
"""
import os
import sys

sys.path.append(os.path.abspath('/Users/yashwantbhambhani/Documents/SHWAYB/FSTK'))

from fstk_utilities_pkg.data_access_utilities.data_access_util import *
from fstk_utilities_pkg.performance_measurement_utilities.performance_measurement_util import *

'''Volume 2, Chap 01, Eg 02 '''
#arr_stocks_price_data = []
#df_stocks_price_data = []
#arr_stocks_performance_returns = []
#
#obj_arr_stock_price_data = DataAsArray(DatasetTypeList.ARRAY)
#
#arr_stocks_price_data = obj_arr_stock_price_data.getData(s_volume="vol2", \
#s_chapter="chap01", s_example="eg02", \
#s_source_filename="Stocks_Prices", s_source_type="csv", \
#verbose=False)
#
#obj_df_stocks_price_data = DataAsDataFrame(DatasetTypeList.DATAFRAME)
#
#df_stocks_price_data = obj_df_stocks_price_data.getData(s_volume="vol2", \
#s_chapter="chap01", s_example="eg02", \
#s_source_filename="Stocks_Prices", s_source_type="csv", \
#verbose=False)
#
#obj_arr_stocks_performance_returns = \
#    PerformanceMeasurement(s_perf_rtn_type=Performance_Return_Type.LOGNORMAL)
#arr_stocks_performance_returns = \
#    obj_arr_stocks_performance_returns.getPerformanceReturn(arr_stocks_price_data)
#
#print arr_stocks_performance_returns


'''Volume 2, Chap 01, Eg 05 '''
from portfolio_management_utilities.portfolio_management import *
from portfolio_management_utilities.position_util import *
from fstk_utilities_pkg.data_access_utilities.data_access_util import *

arr_Position = []
objPosition = 
objPortfolio = portfolio_management.portfolio("vol02_chap01_eg05_portfolio")

objPortfolio.add()




