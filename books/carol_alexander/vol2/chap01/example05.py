# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 09:46:47 2016

@author: yashwantbhambhani
"""

import math
from fstk_utilities_pkg.portfolio_manager.portfolio import *
from fstk_utilities_pkg.instruments.equity import *
from fstk_utilities_pkg.data_access_utilities.data_access_util import *
from fstk_utilities_pkg.risk_manager.equity_risk import *
from fstk_utilities_pkg.common_utilities.array_util import *

volume = "vol2"
chapter = "chap01"
example = "eg05"

portfolio_name = "port_" + volume + "_" + chapter + "_" + example 
obj_portfolio = portfolio(portfolio_name)

obj_df_risk_factors_data = DataAsDataFrame(DatasetTypeList.DATAFRAME)
obj_df_equity_instruments_data = DataAsDataFrame(DatasetTypeList.DATAFRAME)
obj_df_stocks_betas_data = DataAsDataFrame(DatasetTypeList.DATAFRAME)
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

df_stocks_beta_data = obj_df_stocks_betas_data.getData(\
                                s_volume=volume, s_chapter=chapter,\
                                s_example=example, \
                                s_source_filename="Stocks_Betas", \
                                s_source_type="csv", verbose=False)                                

df_portfolio_data = obj_df_portfolio_data.getData(\
                                s_volume=volume, s_chapter=chapter,\
                                s_example=example, \
                                s_source_filename="Portfolio", \
                                s_source_type="csv", verbose=False)

#Setting universe of risk factors
arr_risk_factors = []

for risk_factor in df_risk_factors_data.index:
    obj_risk_factor = equity_risk_factor(risk_factor,\
                        df_risk_factors_data.ix[risk_factor]['Asset Class'])    
    arr_risk_factors.append(obj_risk_factor)
                                                 
#Setting universe of equity instruments
arr_equity_instruments = []

for equity_instrument in df_equity_instruments_data.index:
    obj_equity = equity_valuation_multi(equity_instrument)
    for risk_factor in arr_risk_factors:
        if risk_factor.getAssetClass() == risk_factor_asset_class.EQT:
            obj_equity.addRiskFactor(risk_factor.getRiskFactorName())
            if (risk_factor.getRiskFactorName() == 'Index1'):
                obj_equity.setRiskFactorSensValue(risk_factor.getRiskFactorName(),\
                        df_stocks_beta_data.ix[equity_instrument]['Beta 1'])
            elif (risk_factor.getRiskFactorName() == 'Index2'):
                obj_equity.setRiskFactorSensValue(risk_factor.getRiskFactorName(),\
                        df_stocks_beta_data.ix[equity_instrument]['Beta 2'])
    arr_equity_instruments.append(obj_equity)

#Creating a new portfolio
obj_portfolio = portfolio(portfolio_name)

#Adding positions to the portfolio
for portfolio_item in df_portfolio_data.index:
    #Get the corresponding equity object from the array of equity objects
    for equity_obj in arr_equity_instruments:
        if equity_obj.getIdentifier() == portfolio_item:
            obj_position = equity_position(equity_obj, position_type.EQT,\
                                df_portfolio_data.ix[portfolio_item]['Weight'],
                                df_portfolio_data.ix[portfolio_item]['Weight'])
            obj_portfolio.addPosition(obj_position)

arr_portfolio_positions = obj_portfolio.getPositions()
arr_portfolio_positions_betas = obj_portfolio.getPositionsBetas()

#Filtering correlations data to get correlation matrix for stocks in the portfolio
##This information should be cached
obj_db = Db()
df_all_risk_factors_correlations = \
                        obj_db.getAllRiskFactorsCorrelations()
                        
#Retrieve all the correlations for the risk factors of the portfolio
lst_portfolio_all_risk_factors = obj_portfolio.getAllRiskFactors()
row_filter = lst_portfolio_all_risk_factors
column_filter = lst_portfolio_all_risk_factors                        
df_portfolio_stocks_risk_factors_correlations = \
            df_all_risk_factors_correlations.ix[row_filter][column_filter]
lst_portfolio_stocks_risk_factors_correlation = \
            df_portfolio_stocks_risk_factors_correlations.values.tolist()
            
#Calculate Variance Covariance Matrix of risk factors
obj_array_util = array_util()
lst_equities_risk_factors = obj_portfolio.getAllRiskFactors()
ser_risk_factors_vol_data = df_risk_factors_data['Volatility']
df_risk_factors_vol_data = pd.DataFrame(ser_risk_factors_vol_data)
mat_portfolio_risk_factors_var_covar = obj_array_util.calc_var_covar_matrix(\
                                obj_portfolio.getAllRiskFactors().tolist(), \
                                df_risk_factors_vol_data,\
                                lst_portfolio_stocks_risk_factors_correlation
                                )
                                
obj_portfolio.setPortfolioRiskFactorsVarCovarMatrix(\
                                mat_portfolio_risk_factors_var_covar)                          

obj_portfolio.calcPortfolioRisk()

print '*************INPUTS**************'
print '*********************************'
print ''
print df_portfolio_data
print '*********************************'
print df_stocks_beta_data
print '*********************************'
print df_risk_factors_data
print ''
print '************OUTPUTS**************'
print '*********************************'
print ''
print '************Net Betas of stocks in portfolio************'
print obj_portfolio.getAllRiskFactors()
print obj_portfolio.getPortfolioBeta()    
print '********************************************************'
print '***********Covariance Matrix of risk factors************'
print mat_portfolio_risk_factors_var_covar
print '*********Portfolio Variance due to risk factors*********'
print obj_portfolio.getPortfolioVariance()
print '*********Portfolio Volatility due to risk factors*********'
print obj_portfolio.getPortfolioVolatility()