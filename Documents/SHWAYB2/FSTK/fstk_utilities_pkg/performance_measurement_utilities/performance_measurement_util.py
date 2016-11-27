# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 07:46:42 2016

@author: yashwantbhambhani
"""

import numpy as np

class Performance_Return_Type(object):
    LOGNORMAL = "lognormal"
    NORMAL = "normal"
    
class PerformanceMeasurement(object):
    def __init__(self, s_perf_rtn_type=Performance_Return_Type.NORMAL):
        
        self.performance_return_type = s_perf_rtn_type
        self.arr_returns = []
        
    def getPerformanceReturn(self, arr_prices_data):
        
        arr_returns = []
        
        for i in xrange(1, len(arr_prices_data)):
            if self.performance_return_type == Performance_Return_Type.LOGNORMAL:
                arr_returns.append(np.log(arr_prices_data[i] / arr_prices_data[i-1]))
            elif self.performance_return_type == Performance_Return_Type.NORMAL:
                arr_returns.append((arr_prices_data[i] / arr_prices_data[i-1])-1)        
                
        print arr_returns
        return arr_returns
   