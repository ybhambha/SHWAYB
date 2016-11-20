# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 22:57:35 2016

@author: yashwantbhambhani
"""
from fstk_utilities_pkg.data_access_utilities.data_access_util import DataAsDataFrame
from fstk_utilities_pkg.data_access_utilities.data_access_util import DatasetTypeList
import pandas as pd


class risk_factor_asset_class(object):
    EQT = "Equity"
    FI = "Fixed Income"
    FX = "FX"
    DERV = "Derivative"
    
class risk_factor_classification(object):
    FOREIGN_MKT_IDX = "Foreign Market Index"
    XCHG_RT = "Exchange Rate"
    EQT = "Equity"
    
class risk_factor(object):
     def __init__(self, s_risk_factor_name_in, s_asset_class_in, f_vol_in):
        self.risk_factor_name = s_risk_factor_name_in
        self.asset_class = s_asset_class_in
        self.volatility = f_vol_in
        
     def setVolatility(self, f_vol_in):
        self.volatility = f_vol_in
        
     def getVolatility(self, s_risk_factor_id_in):
         
         volume = "vol2"
         chapter = "chap01"
         example = "eg05"
         
         risk_factor_id = s_risk_factor_id_in
         
         obj_df_risk_factors_vol_data = DataAsDataFrame(DatasetTypeList.DATAFRAME)
         
         df_risk_factors_data = obj_df_risk_factors_vol_data.getData(s_volume=volume,\
                         s_chapter=chapter,s_example=example, \
                         s_source_filename="Risk_Factors", s_source_type="csv",\
                         verbose=False)
         print df_risk_factors_data.ix[risk_factor_id]['Volatility']
                                  
        #return self.volatility

     def getAssetClass(self):
        return self.asset_class
        
class risk_type:
    BETA = "Beta"
    VOL = "Volatility"
    VARIANCE = "Variance"    
    DUR = "Duration"
    ZVOL_SPD = "Zero Volatility Spread"
    OAS = "Option Adjusted Spread"
    KRD = "Key Rate Duration"

class correlation(object):
    def _init__(self, s_risk_factor_name_1_in, s_risk_factor_name_2_in):
        self.risk_factor_name_1 = s_risk_factor_name_1_in
        self.risk_factor_name_2 = s_risk_factor_name_2_in
        self.df_correlation = pd.DataFrame()
        
    def set_correlation_matrix(self, s_risk_factor_name_1_in, \
                            s_risk_factor_name_2_in, f_corr_value):
        
        df_correlation_data_1 = pd.DataFrame({'s_risk_factor_name_1_in': 1, \
                                's_risk_factor_name_2_in': f_corr_value}, \
                                index = [s_risk_factor_name_1_in])
                                
        df_correlation_data_2 = pd.DataFrame({'s_risk_factor_name_1_in': \
                                                            f_corr_value, \
                                            's_risk_factor_name_2_in': 1}, \
                                index = [s_risk_factor_name_2_in])
                                
        self.df_correlation = df_correlation_data_1.append( \
                                                df_correlation_data_2)
                                                
        return self.df_correlation
        
        
        
    
                
        