# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 07:02:11 2016

@author: yashwantbhambhani
"""

import os

class config:
    def get_data_files_location(self):
        self.data_files_location = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/data/'  
        return self.data_files_location