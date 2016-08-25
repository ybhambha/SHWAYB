# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 08:35:48 2016

@author: yashwantbhambhani
"""
from fstk_utilities_pkg.instruments.equity import *

class position_type(object):
    EQT = "Equity Position"
    FI = "Fixed Income Position"
    FX = "FX Position"
    DERV = "Derivative Position"

class position(object):
    
    def __init__(self, s_pos_identifier, init_qty, init_pos_dt):
        self.position_identifier = s_pos_identifier
        self.quantity = init_qty
        self.position_date = init_pos_dt

    def getType(self):
        '''Logic to retrieve information from reference data, \
        ie. instruments class
        '''
        return self.type
        

    def getPrice(self):
        '''Logic to retrieve price information from prices class
        '''
        return self.price
        
    def getMarketValue(self):
        self.market_value = self.price * self.quantity
        return self.market_value
        
    def getQuantity(self):
        return self.quantity
        
    def getRisks(self):
        
        
class equity_position(position):
    
    def __init__(self, s_eq_pos_identifier, init_eq_qty, arr_eq_risks, \
    init_eq_pos_date):    
        eq_position_inst = equity(s_eq_pos_identifier)
        eq_position_qty = init_eq_qty
        
    def getPrice(self):
        
        
    
    def risk(self):
        
        