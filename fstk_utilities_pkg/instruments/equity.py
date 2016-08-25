# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 08:09:20 2016

@author: yashwantbhambhani
"""

class risk_type:
    BETA = "beta"
    DELTA = "delta"

class equity(object):
    def __init__(self, s_identifier):
        self.identifier = s_identifier
        self.risks = []
        
    def add_risk(self, s_risk_type, s_risk_name):
        self.risks.append(s_risk_type)
        
    def get_risks(self):
        return self.risks