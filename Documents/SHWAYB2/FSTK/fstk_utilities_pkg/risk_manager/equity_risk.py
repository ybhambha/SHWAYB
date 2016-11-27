# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 19:25:47 2016

@author: yashwantbhambhani
"""
import logging
import pandas as pd
from fstk_utilities_pkg.risk_manager.risk import *

class equity_risk_factor_type:
    SYSTEM_RISK = "Systematic Risk"
    SPECIFIC_RISK = "Specific Risk"
    BETA = "Beta"
    VOL = "Volatility"
    
class equity_risk_model:
    SINGLE_RISK_FACTOR_MODEL = "Single Risk Factor Model"
    MULTI_RISK_FACTOR_MODEL = "Multiple Risk Factor Model"
    
class equity_risk_factor(risk_factor):

    def __init__(self, s_risk_factor_name_in, s_asset_class_in, f_vol_in=None):
        risk_factor.__init__(self, s_risk_factor_name_in, s_asset_class_in, \
                                f_vol_in) 
        
        LOG_FILENAME = 'example.log'
        logging.basicConfig(filename=LOG_FILENAME,level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        
        self.df_risk_factors = pd.DataFrame(columns=['risk_factor'])
        self.df_risk_factors_sens = pd.DataFrame(columns=['risk_factor', \
                                                        'risk_factor_sens'])
        self.name = s_risk_factor_name_in
        self.volatility = 0
        
    def getRiskFactorName(self):
        return self.name
    
    def getRiskFactorVolatility(self):
        print 'risk_manager-->equity_risk.py-->equity_risk_factor-->\
                    getRiskFactorVolatility'
    
    def addRiskFactor(self, s_risk_factor_name_in):
        df1 = self.df_risk_factors      
        df_risk_factor_data = pd.DataFrame({'risk_factor': \
                                            s_risk_factor_name_in}, \
                                            index = [s_risk_factor_name_in])
                
        df2 = df1.append(df_risk_factor_data)
        self.df_risk_factors = df2
        
    def getRiskFactors(self):
        return self.df_risk_factors
        
    def setRiskFactorSensValue(self, s_risk_factor_name_in, \
                                f_risk_factor_sens_value_in):
        df1 = self.df_risk_factors_sens
        df_risk_factor_sens_data = pd.DataFrame({'risk_factor': \
                                                s_risk_factor_name_in, \
                                                'risk_factor_sens': \
                                                f_risk_factor_sens_value_in}, \
                                                index = [s_risk_factor_name_in])        
        df2 = df1.append(df_risk_factor_sens_data)        
        self.df_risk_factors_sens = df2
        
        self.logger.info(self.df_risk_factors_sens)
        
    def getRiskFactorSensValue(self, s_equity_risk_factor_name_in):
        return self.df_risk_factors_sens['risk_factor_sens'] \
                                        [s_equity_risk_factor_name_in]
        