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
    
    def __init__(self, position_inst_in, position_type_in, f_qty_in, \
                f_mkt_val_in):
        self.position_inst = position_inst_in
        self.position_type = position_type_in
        self.quantity = f_qty_in
        self.market_value = f_mkt_val_in
        
        if s_position_type_in == position_type.EQT:
            m_inst = equity_valuation_multi(s_position_inst_in)
            
        self.position_inst = m_inst

    def getType(self):
        '''Logic to retrieve information from reference data, \
        ie. instruments class
        '''
        return self.type
        
    def getInstrument(self):
        return self.position_inst
        
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
        print "position.py-->class position: getRisks"
        
class equity_position(position):
    
    def __init__(self, eq_instrument_in, s_position_type_in, f_qty_in, \
                f_mkt_val_in):    
        self.eq_position_inst = eq_instrument_in
        self.position_type = s_position_type_in
        self.eq_position_qty = f_qty_in
        self.eq_position_mkt_val = f_mkt_val_in
        
    def getInstrument(self):
        return self.eq_position_inst
        
    def getQuantity(self):
        return self.eq_position_qty
    
    def getPrice(self):
        print "position.py-->class equity_position: getPrice"
        
    def getEquityRisk(self):
        print "position.py-->class equity_position: getEquityRisk"
        