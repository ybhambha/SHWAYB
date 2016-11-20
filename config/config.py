# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 07:02:11 2016

@author: yashwantbhambhani
"""

import os

class config:
    def get_data_files_location(self):
        data_files_location = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/data/'  
        return data_files_location
        
    def get_yahoo_data_path(self):
        yahoo_data_path = self.get_data_files_location() + '/yahoo'
        return yahoo_data_path