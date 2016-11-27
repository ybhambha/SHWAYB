# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 19:29:31 2016

@author: yashwantbhambhani
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 08:05:22 2016

@author: yashwantbhambhani
"""

import os
import sys
import pandas as pd
import numpy as np

sys.path.append(os.path.abspath('/Users/yashwantbhambhani/Documents/SHWAYB/FSTK'))

import math

from fstk_utilities_pkg.portfolio_manager.portfolio import *
from fstk_utilities_pkg.instruments.instrument import *
from fstk_utilities_pkg.instruments.equity import *
from fstk_utilities_pkg.data_access_utilities.data_access_util import *
from fstk_utilities_pkg.risk_manager.equity_risk import *
from fstk_utilities_pkg.common_utilities.array_util import *

volume = "vol2"
chapter = "chap01"
example = "eg06"

portfolio_name = "portfolio_" + volume + "_" + chapter + "_" + example 
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

obj_db = Db()

for portfolio_instrument in df_portfolio_data.index:
    lst_instrument_risk_factors = obj_db.\
                                getInstrumentRiskFactors_db(portfolio_instrument)
    instrument_type = obj_db.getInstrumentType_db(portfolio_instrument)
    if  (instrument_type == InstrumentType.EQT):   
        obj_equity = equity_valuation_multi(portfolio_instrument)
        
        for risk_factor_name in lst_instrument_risk_factors:
            risk_factor_type = obj_db.getRiskFactorType_db(risk_factor_name)
            obj_risk_factor = equity_risk_factor(risk_factor_name,\
                                                    risk_factor_type)
            obj_equity.addRiskFactor(obj_risk_factor)
            
        obj_position = equity_position(obj_equity, position_type.EQT,\
                    df_portfolio_data.ix[portfolio_instrument]['Holding'],
                    df_portfolio_data.ix[portfolio_instrument]['Holding'])
        obj_portfolio.addPosition(obj_position)
            
print '************OUTPUTS**************'
print '*********************************'
print '***********Net Portfolio Beta**********'
print obj_portfolio.getNetPortfolioBetaOnEachFactor()
print ''
print '***********Systematic Variance of the portfolio**********'
print obj_portfolio.getPortfolioSystematicVariance()
print '' 
print '***********Systematic Risk of the portfolio**********'
print obj_portfolio.getPortfolioSystematicRisk()
print ''
print '***********Equity Variance of the portfolio**********'
print obj_portfolio.getPortfolioSystematicVariance(risk_factor_classification.FOREIGN_MKT_IDX,\
                                                    risk_factor_classification.FOREIGN_MKT_IDX)
print '' 
print '***********Equity Risk of the portfolio**********'
print obj_portfolio.getPortfolioSystematicRisk(risk_factor_classification.FOREIGN_MKT_IDX, \
                                                    risk_factor_classification.FOREIGN_MKT_IDX)
print ''
print '***********FX Variance of the portfolio**********'
print obj_portfolio.getPortfolioSystematicVariance(risk_factor_classification.XCHG_RT, \
                                                    risk_factor_classification.XCHG_RT)
print '' 
print '***********FX Risk of the portfolio**********'
print obj_portfolio.getPortfolioSystematicRisk(risk_factor_classification.XCHG_RT, \
                                                    risk_factor_classification.XCHG_RT)                                                       
print ''
print '***********Quanto Variance of the portfolio**********'
print obj_portfolio.getPortfolioSystematicVariance(risk_factor_classification.FOREIGN_MKT_IDX, \
                                                    risk_factor_classification.XCHG_RT)
print '' 
print '***********Quanto Risk of the portfolio**********'
print obj_portfolio.getPortfolioSystematicRisk(risk_factor_classification.FOREIGN_MKT_IDX, \
                                                    risk_factor_classification.XCHG_RT)