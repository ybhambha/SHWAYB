# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 18:55:07 2016

@author: yashwantbhambhani
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 08:09:20 2016

@author: yashwantbhambhani
"""
import pandas as pd
import logging
from fstk_utilities_pkg.risk_manager.equity_risk import *
from fstk_utilities_pkg.instruments.derivative import *
from fstk_utilities_pkg.data_access_utilities.data_access_util import *

class equity_valuation:
    def __init__(self, s_identifier_in):
        
        LOG_FILENAME = 'example.log'
        logging.basicConfig(filename=LOG_FILENAME,level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        
        self.identifier = s_identifier_in
        
    def getRisk(self):
        return self.risk

class equity_valuation_multi(equity_valuation):
    
    def __init__(self, s_identifier_in):
                            
        equity_valuation.__init__(self, s_identifier_in)
        
        LOG_FILENAME = 'example.log'
        logging.basicConfig(filename=LOG_FILENAME,level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        
        self.identifier = s_identifier_in
        self.risk_factor_model = equity_risk_model.MULTI_RISK_FACTOR_MODEL
        #self.risk = equity_risk_factor(self.risk_factor_model)
        self.df_risk_factors = pd.DataFrame()
        self.df_risk_factors_sens_value = pd.DataFrame()
        
    def getIdentifier(self):
        print type(self.identifier)
        return self.identifier
                                        
    def getEquities(self):
        print 'equity.py-->equity_valuation_multi: getEquities'
        
    def setRiskFactorSensitivity(self, risk_factor_in):
        print 'equity_valuation_single: setRiskFactorSensitivity'
        
    def addRiskFactor(self, s_risk_factor_name_in):
        
        self.logger.info('Risk Factor To Be Added'+s_risk_factor_name_in)       
#        risk_factor_name = s_risk_factor_name_in
        
#        m_risk_factor = equity_risk_factor(risk_factor_name)
#        self.risk_factors.append(m_risk_factor)
        
        
        df1 = self.df_risk_factors      
        df_risk_factor_data = pd.DataFrame({'risk_factor': \
                                            s_risk_factor_name_in}, \
                                            index = [s_risk_factor_name_in])
                
        df2 = df1.append(df_risk_factor_data)
        self.df_risk_factors = df2
        
    def getRiskFactors(self):
        return self.df_risk_factors
    
    def getRiskFactorsFromDb(object):
        self.logger.info('Retrieving Risk Factor information from Db')
        obj_risk_factors_db = RiskFactors_Db()
        df_equity_risk_factors = obj_risk_factors_db.getEquityRiskFactors(\
                                            [self.getIdentifier])
        return df_equity_risk_factors
    
    def setRiskFactorSensValue(self, s_risk_factor_name_in, \
                                f_risk_factor_sens_value_in):
        
        self.logger.info('Risk Factor Sensitivity to be set'+\
                    s_risk_factor_name_in + str(f_risk_factor_sens_value_in))
        
        df1 = self.df_risk_factors_sens_value
                
        df_risk_factor_sens_value_data = pd.DataFrame({'risk_factor': \
                                                s_risk_factor_name_in, \
                                                'risk_factor_sens': \
                                                f_risk_factor_sens_value_in}, \
                                                index = [s_risk_factor_name_in])        
        df2 = df1.append(df_risk_factor_sens_value_data)        
        self.df_risk_factors_sens_value = df2
        
    def getRiskFactorSensValue(self, s_equity_risk_factor_name_in=None):
        
        self.logger.info('Retrieving sens value for '+\
                            self.getIdentifier())
                            
        print self.df_risk_factors_sens_value
        
        if (s_equity_risk_factor_name_in == None):
            return self.df_risk_factors_sens_value
        else:
            return self.df_risk_factors_sens_value['risk_factor_sens'] \
                                        [s_equity_risk_factor_name_in]                                    
        
class equity_valuation_single(equity_valuation):
    def get_risk_factors(self):
        print 'equity_valuation_single: get_risk_factors'
    
class equity_option(derivative):
    def get_delta(self):
        print 'equity_option: get_delta'
        
