# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 19:19:00 2016

@author: yashwantbhambhani
"""

class PriceType():
    CLOSE = "Close Price"
    HIGH = "High"
    LOW = "Low"
    ADJ_CLOSE = "Adjusted Close"

class price:
    def __init__(self, s_symbol, s_price_type=PriceType.CLOSE, px_dt):
        self.price_of = s_symbol        
        self.price_type = s_price_type
        self.price_date = px_dt
        
    