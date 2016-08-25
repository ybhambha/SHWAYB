# -*- coding: utf-8 -*-
"""
Created on Sat Aug  6 08:19:03 2016

@author: yashwantbhambhani
"""

class Data_Return_Type:
    def __init__(self, name):
        self.name=name
        
    def getData(self):
        raise NotImplementedError("The child class must have abstract method")
        
class Array_As_Data_Return_Type(Data_Return_Type):
    def getData(self, s_source=DataSource.CAROL_ALEXANDER_BOOK, \
    s_source_type=DataSourceType.CSV, s_data_return_type=DataReturnType.ARRAY):

        '''
        @param s_source: Default source is data from Carol Alexander's book                
        arr_csv_data = np.genfromtxt(getPathOfCSVFile(s_csv_file_name))
        
        @param s_data_return_type: Default return type is an Array
        
        '''
        
        arrData = np.genfromtxt ()
        
        