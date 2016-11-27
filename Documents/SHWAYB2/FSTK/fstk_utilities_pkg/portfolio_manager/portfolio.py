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
from fstk_utilities_pkg.risk_manager.risk import *
from fstk_utilities_pkg.common_utilities.array_util import *

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
        
        self.obj_db = Db()
        
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
        arr_positions_mktval = []
        for position_no in range(len(self.port_positions)):
            arr_positions_mktval.append(self.port_positions[position_no].getQuantity())

        self.arr_positions_weights = arr_positions_mktval / np.sum(arr_positions_mktval)
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
        
    def getPositionsBetas_db(self):
        beta_index = []
        
        for position_no in range(len(self.port_positions)):
            self.logger.info(type(self.port_positions[position_no].\
                                   getInstrument()))     
            for risk_factor_name in self.port_positions[position_no].\
                                    getInstrument().getRiskFactorsNames():
                if (self.obj_db.getRiskFactorType_db(risk_factor_name)\
                    == risk_factor_classification.FOREIGN_MKT_IDX):
                        beta_index.append(self.obj_db.\
                        getStockInstrumentBeta_db(self.port_positions[position_no].\
                        getInstrument().getIdentifier()))

        self.arr_positions_betas.append(np.array(beta_index))
        
        return self.arr_positions_betas
    
    def getPositions(self):
        return self.port_positions
        
    def addPosition(self, pos_in):
        m_pos = pos_in
        self.port_positions.append(m_pos)
        #Recalculate the weights of all the positions including the one just added
    
    def getAllPositionsInstrumentNames(self):
        arr_portfolio_all_positions_instrument_names = []
        
        for portfolio_position in self.getPositions():
            arr_portfolio_all_positions_instrument_names.append(portfolio_position.getInstrument().getIdentifier())
 
        return  arr_portfolio_all_positions_instrument_names          
    
    def getAllRiskFactors(self):
        self.arr_portfolio_all_risk_factors = []
        
        for portfolio_position in self.getPositions():
            for portfolio_position_risk_factor in portfolio_position.getInstrument().getRiskFactors():
                self.arr_portfolio_all_risk_factors.append(portfolio_position_risk_factor)

        return self.arr_portfolio_all_risk_factors
        
    def getAllRiskFactorsNames(self, s_factor_type_1_filter_in = None):
        arr_portfolio_all_risk_factors_names = []
        
        if (s_factor_type_1_filter_in == None):
            for portfolio_position in self.getPositions():
                for portfolio_position_risk_factor in portfolio_position.getInstrument().getRiskFactors():
                    arr_portfolio_all_risk_factors_names.append(portfolio_position_risk_factor.getRiskFactorName())
            return list(set(arr_portfolio_all_risk_factors_names))
#        elif (s_factor_type_1_filter_in == risk_factor_classification.FOREIGN_MKT_IDX):
#            arr_portfolio_all_risk_factors_names = self.getAllRiskFactorsNames()
#            arr_portfolio_equity_risk_factors_names = []
#            
#            for risk_factor_name in arr_portfolio_all_risk_factors_names:
#                if (self.obj_db.getRiskFactorType_db(risk_factor_name) == \
#                                    risk_factor_classification.FOREIGN_MKT_IDX):
#                                        arr_portfolio_equity_risk_factors_names.append(risk_factor_name)
#            return arr_portfolio_equity_risk_factors_names
        else:
            arr_portfolio_all_risk_factors_names = self.getAllRiskFactorsNames()
            arr_portfolio_filter_risk_factors_names = []
            
            for risk_factor_name in arr_portfolio_all_risk_factors_names:
                if (self.obj_db.getRiskFactorType_db(risk_factor_name) == \
                                    s_factor_type_1_filter_in):
                                        arr_portfolio_filter_risk_factors_names.append(risk_factor_name)
            return list(set(arr_portfolio_filter_risk_factors_names))
    
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
            self.arr_positions_betas = self.getPositionsBetas_db()
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
        
    def getBetaMatrix(self):
        #Create Beta matrix for portfolio equity positions
        beta_zeros = np.zeros(shape=(len(self.getAllRiskFactorsNames()),\
                                    len(self.getAllPositionsInstrumentNames())))
        
        df_beta_matrix = pd.DataFrame(beta_zeros,\
                                columns=self.getAllPositionsInstrumentNames(),\
                                index=self.getAllRiskFactorsNames())
        for instrument_name in self.getAllPositionsInstrumentNames():
            for risk_factor_name in self.obj_db.getInstrumentRiskFactors_db(instrument_name):
                if (self.obj_db.getRiskFactorType_db(risk_factor_name) == risk_factor_classification.XCHG_RT):
                    df_beta_matrix.ix[risk_factor_name][instrument_name] = 1
                elif (self.obj_db.getRiskFactorType_db(risk_factor_name) == risk_factor_classification.FOREIGN_MKT_IDX):
                    df_beta_matrix.ix[risk_factor_name][instrument_name] = self.obj_db.getStockInstrumentBeta_db(instrument_name)
        
        return df_beta_matrix
        
    def getNetPortfolioBetaOnEachFactor(self, s_factor_type_1_filter_in = None):
        if (s_factor_type_1_filter_in == None):        
            return pd.DataFrame(np.array(self.getBetaMatrix().dot(self.getPositionsWeights())), \
                                index = self.getAllRiskFactorsNames(), \
                                columns=['Net Portfolio Beta'] \
                                )
        else:
            equity_risk_factors_beta_matrix = self.getBetaMatrix().\
                                    ix[self.getAllRiskFactorsNames(s_factor_type_1_filter_in)]      
            return pd.DataFrame(np.array(equity_risk_factors_beta_matrix.dot(self.getPositionsWeights())), \
                            index = self.getAllRiskFactorsNames(s_factor_type_1_filter_in), \
                            columns=['Net Portfolio Beta'] \
                            )
                            
    def getPortfolioRiskFactorsVarianceCovariance(self, \
                                            s_factor_type_1_filter_in = None, \
                                            s_factor_type_2_filter_in = None):
        #Calculate Variance Covariance Matrix of risk factors
        obj_array_util = array_util()
        
        df_risk_factors_volatility_db = self.obj_db.getRiskFactorsVolatility_db(\
                                self.getAllRiskFactorsNames()\
                                )
        
        mat_portfolio_risk_factors_var_covar = \
                                obj_array_util.calc_var_covar_matrix(\
                                self.getAllRiskFactorsNames(), \
                                df_risk_factors_volatility_db,\
                                self.obj_db.getRiskFactorsCorrelations_db\
                                (self.getAllRiskFactorsNames()).values.tolist())
                                
        risk_factors_type_1_names = self.getAllRiskFactorsNames(\
                                                    s_factor_type_1_filter_in)
                                                    
        risk_factors_type_2_names = self.getAllRiskFactorsNames(\
                                                    s_factor_type_2_filter_in)
        
        if (s_factor_type_1_filter_in == None):
            return mat_portfolio_risk_factors_var_covar
        else:
            mat_portfolio_risk_factors_type_1_2_var_covar = \
                                mat_portfolio_risk_factors_var_covar.ix[risk_factors_type_1_names]\
                                [risk_factors_type_2_names]
            return mat_portfolio_risk_factors_type_1_2_var_covar
                        
    def getPortfolioSystematicVariance(self, s_factor_type_1_filter_in = None,\
                                        s_factor_type_2_filter_in = None):
        
        return float(\
                np.array(self.getNetPortfolioBetaOnEachFactor(s_factor_type_1_filter_in)).transpose().dot\
                (np.array(self.getPortfolioRiskFactorsVarianceCovariance(s_factor_type_1_filter_in, s_factor_type_2_filter_in))).dot\
                (np.array(self.getNetPortfolioBetaOnEachFactor(s_factor_type_2_filter_in)))\
                )
                
    def getPortfolioSystematicRisk(self, s_factor_type_1_filter_in = None, \
                                        s_factor_type_2_filter_in = None):
        return math.pow(self.getPortfolioSystematicVariance(\
                                        s_factor_type_1_filter_in,
                                        s_factor_type_2_filter_in\
                                        ), 0.5)
        
    