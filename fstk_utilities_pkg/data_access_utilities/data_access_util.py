# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 07:40:53 2016

@author: yashwantbhambhani
"""

import numpy as np
import pandas as pd
import os
import csv
from config.config import *

class DataSource(object):
    CAROL_ALEXANDER_BOOK = "carol_alexander_book"
    YAHOO = "yahoo"
    
class DataSourceType(object):
    XLS = "xls"
    CSV = "csv"
    XML = "xml"
    
class DatasetTypeList(object):
    DATAFRAME = "DataFrame"
    ARRAY = "Array"
    
class DataReturnType(object):
    def __init__(self, name):
        self.name=name
        
    def getData(self):
        raise NotImplementedError("The child class must have abstract method")
   
class DataAccess:
    def __init__(self, s_source='carol_alexander_book', s_data_path=None, \
    s_volume=None, s_example=None, verbose=False):
        '''
        @param s_source: All the paths are initialized based on the source 
            specified. The path to CAROL_ALEXANDER_BOOK is the default one.
        '''
        
        obj_config = config()
        
        self.folder_list = list()
        self.folder_sub_list = list()
        
        if s_data_path != None:
            self.root_dir = s_data_path
        else:
            self.root_dir = os.path.join(os.path.dirname(__file__), '..', \
            '/data/')
        
        self.script_path = os.path.abspath('__file__')
        self.script_dir = os.path.split(self.script_path)[0] 
        
        if verbose:
            print "Data Directory", self.source_path
        
        if s_source==DataSource.CAROL_ALEXANDER_BOOK:
            #self.source_path = self.root_dir + DataSource.CAROL_ALEXANDER_BOOK + "/"
            self.source_path = obj_config.get_data_files_location() + DataSource.CAROL_ALEXANDER_BOOK + '/'
            self.folder_sub_list.append('/vol2/chap01/')
            self.folder_sub_list.append('/vol2/chap02/')
            
            for i in self.folder_sub_list:
                #self.folder_list.append(self.root_dir + self.source_path + i)
                self.folder_list.append(self.script_dir + self.source_path + i)

        elif s_source==DataSource.YAHOO:
            #self.source_path = self.root_dir + DataSource.CAROL_ALEXANDER_BOOK + "/"
            self.source_path = obj_config.get_data_files_location() + DataSource.CAROL_ALEXANDER_BOOK + "/"
        else:
            raise ValueError("Incorrect data requested")
            
    def getPathOfCSVFile(self, s_csv_file_name, verbose=False):

        for path1 in self.folder_list:
                if (os.path.exists(str(path1)+str(s_csv_file_name+".csv"))):
                    return (str(str(path1)+str(s_csv_file_name)+".csv"))
                    
        print "Did not find path to " + str (s_csv_file_name)+". Looks like this \
        file is missing"
        
class DataAsArray(DataReturnType):
    def getData(self, \
    s_volume, s_chapter, s_example, s_source_filename=None, \
    s_source_type='csv', s_source=DataSource.CAROL_ALEXANDER_BOOK, \
    dtype_in=None, verbose=False):

        '''
        @param s_source: Default source is data from Carol Alexander's book                
        arr_csv_data = np.genfromtxt(getPathOfCSVFile(s_csv_file_name))

        returns data from the source file in the form of a numpy array        
        '''   
        da = DataAccess()

        if s_source==DataSource.CAROL_ALEXANDER_BOOK:
            if s_source_type == DataSourceType.CSV:
                if s_source_filename == None:
                    arr_data = np.genfromtxt(da.source_path + s_volume + '/' \
                    + s_chapter + '/' + s_example + '/' + '.' + s_source_type, 
                    delimiter=",", dtype=dtype_in)
                else:
                    arr_data = np.genfromtxt(da.source_path + s_volume + \
                    '/' + s_chapter + '/' + s_example + '/' + s_source_filename \
                    + '.' + s_source_type, delimiter=",", dtype=dtype_in)
            else:
                print "Logic for non CSV File from Carol Alexander's book"
        else:
            print "Logic for XYX source"
            
        return arr_data
            
class DataAsDataFrame(DataReturnType):
    def getData(self, s_volume, s_chapter, s_example, s_source_filename, \
    s_source=DataSource.CAROL_ALEXANDER_BOOK, \
    s_source_type=DataSourceType.CSV, verbose=False):
        
        '''
        Returns data from the source file in the form of a DataFrame object
        '''
        da = DataAccess()
        
        if s_source==DataSource.CAROL_ALEXANDER_BOOK:
            if s_source_type == DataSourceType.CSV:
                if s_source_filename == None:
                    df_data = pd.read_csv(da.source_path + s_volume + '/' \
                    + s_chapter + '/' + s_example + '/' + s_source_filename + \
                    + '.' + s_source_type)
                else:
                    df_data = pd.read_csv(da.source_path + s_volume + \
                    '/' + s_chapter + '/' + s_example + '/' + s_source_filename \
                    + '.' + s_source_type)
            else:
                print "Logic for non CSV File from Carol Alexander's book"
        else:
            print "Logic for XYX source"
                
        return df_data
