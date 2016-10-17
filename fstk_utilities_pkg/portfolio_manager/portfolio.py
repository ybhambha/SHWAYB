# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 19:10:34 2016

@author: yashwantbhambhani
"""
import logging
import pandas as pd
import numpy as np
import math
from position import * 

class portfolio(object):
    def __init__(self, s_name):
        
        LOG_FILENAME = 'example.log'
        logging.basicConfig(filename=LOG_FILENAME,level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        
        self.name = s_name
        self.market_value = 0
        self.arr_positions_weights = []
        self.arr_positions_betas = []
        self.net_betas = []
        self.port_positions = []
        self.portfolio_risk_factors = []
        self.portfolio_beta = []
        self.port_var_covar_matrix = []
        self.portfolio_variance = 0
        self.portfolio_volatility = 0
        self.portfolio_risk_factors_volatility = []
        
    def getName(self):
        return self.name
    
    def getPerformance(self):
        arrPerformance = []
        return arrPerformance
    
    def getComposition(self):
        arrComposition = []
        return arrComposition
         
    def getMarketValue(self):
        return self.market_value
        
    def getPositionsWeights(self):
        for position_no in range(len(self.port_positions)):
            self.arr_positions_weights.append(self.port_positions[position_no].\
                                                            getQuantity())
        return self.arr_positions_weights
        
    def getPositionsBetas(self):
        beta_index1 = []
        beta_index2 = []
        
        for position_no in range(len(self.port_positions)):
            self.logger.info(type(self.port_positions[position_no].\
                                   getInstrument()))     
            
            beta_index1.append(self.port_positions[position_no].\
                                   getInstrument().\
                                   getRiskFactorSensValue('Index1'))
                        
            beta_index2.append(self.port_positions[position_no].\
                                   getInstrument().\
                                   getRiskFactorSensValue('Index2'))

        self.arr_positions_betas.append(np.array(beta_index1))
        self.arr_positions_betas.append(np.array(beta_index2))
         
        return self.arr_positions_betas
    
    def getPositions(self):
        return self.port_positions
        
    def addPosition(self, pos_in):
        m_pos = pos_in
        self.port_positions.append(m_pos)    
    
    def getAllRiskFactors(self):
        df_portfolio_all_risk_factors = pd.DataFrame()
        
        for position in self.port_positions:
            df = pd.DataFrame()
            df = position.getInstrument().getRiskFactors()
            df_portfolio_all_risk_factors = df_portfolio_all_risk_factors.append(df)
        
        lst_portfolio_all_risk_factors = pd.unique(df_portfolio_all_risk_factors\
                                            ['risk_factor'].values.ravel())
        self.portfolio_risk_factors = lst_portfolio_all_risk_factors

        return self.portfolio_risk_factors
        
    def getAllRiskFactorsVolatility(self):
                
        for risk_factor in self.portfolio_risk_factors:
            position_id = position.getInstrument().identifier
            #getRisk().getVolatility('Index1')
            print (position_id)
            
            print position.getInstrument().df_risk_factors        
    
    def setPortfolioRiskFactorsVarCovarMatrix(self, port_var_covar_matrix_in):
        self.port_var_covar_matrix = port_var_covar_matrix_in
    
    def calcPortfolioRisk(self):
        self.calcPortfolioBeta()
        self.calcPortfolioVariance()
        self.calcPortfolioVolatility()
        
    def calcPortfolioBeta(self):
        if len(self.arr_positions_weights) == 0:     
            self.arr_positions_weights = self.getPositionsWeights()
        if len(self.arr_positions_betas) == 0:
            self.arr_positions_betas = self.getPositionsBetas()
        m_arr_positions_weights_transp = np.array(self.arr_positions_weights)\
                                                .transpose()
        m_arr_positions_betas  = np.array(self.arr_positions_betas)
        self.portfolio_beta = m_arr_positions_betas.dot(m_arr_positions_weights_transp)
        
    def getPortfolioBeta(self):
        return self.portfolio_beta
    
    def calcPortfolioVariance(self):
        arr_portfolio_beta = self.getPortfolioBeta()
        mat_portfolio_variance = np.mat(np.dot(\
                    np.dot\
                        (np.transpose(arr_portfolio_beta), self.port_var_covar_matrix), \
                        arr_portfolio_beta\
                    ))
        self.portfolio_variance = mat_portfolio_variance[0,0]
                    
    def getPortfolioVariance(self):    
        return self.portfolio_variance
        
    def calcPortfolioVolatility(self):
        self.portfolio_volatility = math.pow(self.portfolio_variance, 0.5)
        
    def getPortfolioVolatility(self):
        return self.portfolio_volatility
        