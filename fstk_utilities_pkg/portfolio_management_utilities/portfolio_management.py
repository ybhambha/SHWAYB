# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 19:10:34 2016

@author: yashwantbhambhani
"""

class Portfolio(object):
    def __init__(self, s_name):
        self.name = s_name
        self.market_value = 0
        self.variance = 0 
        self.volatility = 0 
        self.risk_factors = []
        self.weights = []
        self.positions = []

    def getPerformance(self):
        arrPerformance = []
        return arrPerformance
    
    def getComposition(self):
        arrComposition = []
        return arrComposition
         
    def getMarketValue(self):
        return self.market_value
        
    def getWeights(self):
        arrWeights = []
        return arrWeights
        
    def getPositions(self):
        return self.positions
        
    def addPosition(self, position_in=None):
        self.positions.append(position_in)
    
    #def setWeights(self):
    
    #def getEfficientFronties(self):