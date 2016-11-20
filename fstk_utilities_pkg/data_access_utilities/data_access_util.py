# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 07:40:53 2016

@author: yashwantbhambhani
"""
import numpy as np
import pandas as pd
import pandas_datareader.data as web
import os
import csv
import math    
import logging

from datetime import date, datetime, timedelta
from config.config import *

class DataSource(object):
    CAROL_ALEXANDER_BOOK = "carol_alexander_book"
    YAHOO = "yahoo"
    db = "db"
    
class DataSourceType(object):
    XLS = "xls"
    CSV = "csv"
    XML = "xml"
    
class DatasetTypeList(object):
    DATAFRAME = "DataFrame"
    ARRAY = "Array"
    
class DataReturnType(object):
    def __init__(self, name):
        LOG_FILENAME = 'example.log'
        logging.basicConfig(filename=LOG_FILENAME,level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        
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
            'data')
        
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
            self.source_path = obj_config.get_data_files_location() + DataSource.YAHOO + "/"
        elif s_source==DataSource.db:
            self.source_path = obj_config.get_data_files_location() + DataSource.db + "/"                             
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
        
        self.logger.info(s_volume + s_chapter + s_example + s_source_filename + s_source \
                        + s_source_type)
        
        s_source_to_use = s_source
        
        '''
        Returns data from the source file in the form of a DataFrame object
        '''
        da = DataAccess(s_source_to_use)
  
        if s_source==DataSource.CAROL_ALEXANDER_BOOK:
            if s_source_type == DataSourceType.CSV:
                if s_source_filename == None:
                    print 'Name of Source File not provided'
#                    df_data = pd.read_csv(da.source_path + s_volume + '/' \
#                    + s_chapter + '/' + s_example + '/' + s_source_filename + \
#                    + '.' + s_source_type, index_col = [0])
                else:
                    df_data = pd.read_csv(da.source_path + s_volume + '/' \
                    + s_chapter + '/' + s_example + '/' + s_source_filename + \
                    '.' + s_source_type, index_col = [0])
            else:
                print "Logic for non CSV File from Carol Alexander's book"
        elif s_source==DataSource.db:
            df_data = pd.read_csv(da.source_path + s_source_filename \
                    + '.' + s_source_type, index_col = [0])
        else:
            print "Logic for XYX source"
            print da.source_path + s_volume + '/' \
                    + s_chapter + '/' + s_example + '/' + s_source_filename \
                    + '.' + s_source_type
                
        return df_data
        
class Db(object):
    
    def __init__(self):
        LOG_FILENAME = 'example.log'
        logging.basicConfig(filename=LOG_FILENAME,level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        
    def getAllRiskFactorsCorrelations(self):
        
        volume = "vol2"
        chapter = "chap01"
        example = "eg05"

        obj_df_risk_factors_correlation_data = DataAsDataFrame(DatasetTypeList.DATAFRAME)
        df_risk_factors_correlation_data = obj_df_risk_factors_correlation_data.getData(\
                                        s_volume=volume, s_chapter=chapter,\
                                        s_example=example, \
                                        s_source_filename="Risk_Factors_Correlation", \
                                        s_source_type="csv", verbose=False)
        
        #Get the entire list of instruments for which correlation data exists
        lst_inst_in_db_having_correlation = {}
        lst_inst_in_db_having_correlation = ['Index1', 'Index2', 'Index3']
        f_inst_count = len(lst_inst_in_db_having_correlation)
        
        #Create a square matrix with 1's
        arr_correlations = np.ones((f_inst_count, f_inst_count), dtype='f')
        df_correlations = pd.DataFrame(arr_correlations, \
                        columns=lst_inst_in_db_having_correlation, \
                        index=lst_inst_in_db_having_correlation)
                        
        for correlation_id in df_risk_factors_correlation_data.index:
            risk_factor_1 = df_risk_factors_correlation_data.ix[correlation_id]['Risk factor 1']
            risk_factor_2 = df_risk_factors_correlation_data.ix[correlation_id]['Risk factor 2']
            df_correlations[risk_factor_1][risk_factor_2] = \
                df_risk_factors_correlation_data.ix[correlation_id]['Correlation']
            df_correlations[risk_factor_2][risk_factor_1] = \
                df_risk_factors_correlation_data.ix[correlation_id]['Correlation']
        
        return df_correlations
        
    def getAllRiskFactorsCorrelations_db(self):
       
        obj_df_risk_factors_correlation_data = DataAsDataFrame(DatasetTypeList.DATAFRAME)
        df_risk_factors_correlation_data_db = obj_df_risk_factors_correlation_data.getData(\
                                        s_volume="", s_chapter="",\
                                        s_example="", \
                                        s_source=DataSource.db,\
                                        s_source_filename="db_Risk_Factors_Correlation", \
                                        s_source_type="csv", verbose=False)
        
        arr_risk_factor1_in_db_having_correlation = \
            pd.unique(df_risk_factors_correlation_data_db['Risk factor 1'].values\
                .ravel())
                
        lst_risk_factor1_in_db_having_correlation = \
            arr_risk_factor1_in_db_having_correlation.tolist()
                
        arr_risk_factor2_in_db_having_correlation = \
            pd.unique(df_risk_factors_correlation_data_db['Risk factor 2'].values\
                .ravel())
                
        lst_risk_factor2_in_db_having_correlation = \
            arr_risk_factor2_in_db_having_correlation.tolist()
        
        #Get the entire list of risk factors for which correlation data exists
        lst_risk_factors_in_db_having_correlation = {}
        lst_risk_factors_in_db_having_correlation = \
                 lst_risk_factor1_in_db_having_correlation + \
                 lst_risk_factor2_in_db_having_correlation
                 
        #Get unique list of risk factors for which correlation data exists
        lst_unique_risk_factors_in_db_having_correlation = \
            [ \
            element_e
            for index_i, element_e in enumerate(lst_risk_factors_in_db_having_correlation)
                if lst_risk_factors_in_db_having_correlation.index(element_e) == index_i
            ]
                 
        f_inst_count = len(lst_unique_risk_factors_in_db_having_correlation)
        
        #Create a square matrix with 1's
        arr_correlations = np.ones((f_inst_count, f_inst_count), dtype='f')
        df_correlations = pd.DataFrame(arr_correlations, \
                columns=lst_unique_risk_factors_in_db_having_correlation, \
                index=lst_unique_risk_factors_in_db_having_correlation)
                
        for correlation_id in df_risk_factors_correlation_data_db.index:
            risk_factor_1 = df_risk_factors_correlation_data_db.ix[correlation_id]['Risk factor 1']
            risk_factor_2 = df_risk_factors_correlation_data_db.ix[correlation_id]['Risk factor 2']
            df_correlations[risk_factor_1][risk_factor_2] = \
                df_risk_factors_correlation_data_db.ix[correlation_id]['Correlation']
            df_correlations[risk_factor_2][risk_factor_1] = \
                df_risk_factors_correlation_data_db.ix[correlation_id]['Correlation']
                
        return df_correlations
        
    def getRiskFactorsCorrelations_db(self, lst_risk_factors_in):
        
        row_filter = lst_risk_factors_in
        column_filter = lst_risk_factors_in

        df_all_risk_factors_correlations =  self.getAllRiskFactorsCorrelations_db()                       
        df_risk_factors_correlations_db = \
                    df_all_risk_factors_correlations.ix[row_filter][column_filter]

        return df_risk_factors_correlations_db

        
    def getAllRiskFactorsVolatility_db(self):
        obj_df_risk_factors_data_db = DataAsDataFrame(DatasetTypeList.DATAFRAME)
        df_risk_factors_data_db = obj_df_risk_factors_data_db.getData(\
                                        s_volume="", s_chapter="",\
                                        s_example="", \
                                        s_source=DataSource.db,\
                                        s_source_filename="db_Risk_Factors", \
                                        s_source_type="csv", verbose=False)
        df_risk_factors_volatility_db = df_risk_factors_data_db[['Volatility']]
        return df_risk_factors_volatility_db
        
    def getRiskFactorsVolatility_db(self, lst_risk_factors_in):
        
        row_filter = lst_risk_factors_in
        
        df_all_risk_factors_volatility =  self.getAllRiskFactorsVolatility_db()                       
        df_risk_factors_volatility_db = \
                    df_all_risk_factors_volatility.ix[row_filter]

        return df_risk_factors_volatility_db

    
    def getEquityRiskFactors(self, lst_equity_in = None):
        volume = "vol2"
        chapter = "chap01"
        example = "eg05"
        
        obj_df_equity_risk_factors_data = DataAsDataFrame(DatasetTypeList.DATAFRAME)
        df_equity_risk_factors_data = obj_df_equity_risk_factors_data.getData(\
                                        s_volume=volume, s_chapter=chapter,\
                                        s_example=example, \
                                        s_source_filename="Stocks_Risk_Factors", \
                                        s_source_type="csv", verbose=False)
                                        
        lst_equity = lst_equity_in
        
        if lst_equity_in == None:
            return df_equity_risk_factors_data
        else:
            return df_equity_risk_factors_data.ix[lst_equity]
            
    def addRiskFactorInDb(self, risk_factor_in):
        self.logger.info('Insert risk factor into Db')
        
    def getInstrumentType_db(self, instrument_id_in):
        obj_df_instrument_type_data_db = DataAsDataFrame(DatasetTypeList)
        df_instrument_type_data_db = obj_df_instrument_type_data_db.getData(\
                                        s_volume="", s_chapter="",\
                                        s_example="", \
                                        s_source=DataSource.db,\
                                        s_source_filename="db_Instruments", \
                                        s_source_type="csv", verbose=False)

        instrument_type = df_instrument_type_data_db.ix[instrument_id_in]\
                                                        ['Instrument Type'] 
        return instrument_type                                                
        
    def getInstrumentRiskFactors_db(self, instrument_id_in):
        
        obj_df_instruments_risk_factors_data_db = DataAsDataFrame(DatasetTypeList.DATAFRAME)
        
        df_instruments_risk_factors_data_db = obj_df_instruments_risk_factors_data_db.\
                                        getData(\
                                        s_volume="", s_chapter="",\
                                        s_example="", \
                                        s_source=DataSource.db,\
                                        s_source_filename="db_Instruments_Risk_Factors", \
                                        s_source_type="csv", verbose=False)
       
        df_instrument_risk_factors = df_instruments_risk_factors_data_db.\
                                            ix[instrument_id_in]
                                            
        if (len(df_instrument_risk_factors) == 1):
            #If there is only one row filtered using the index criteria
            #above then df_instrument_risk_factors is already of list type
            return df_instrument_risk_factors
        elif (len(df_instrument_risk_factors) > 1):
            #If there is only one row filtered using the index criteria
            #above then df_instrument_risk_factors is of Series type
            return df_instrument_risk_factors.ix[instrument_id_in]\
                                                ['Risk Factor Id'].tolist()
        
        return df_instrument_risk_factors
        
    def getRiskFactorType_db(self, risk_factor_in):
        
        obj_df_risk_factors_data_db = DataAsDataFrame(DatasetTypeList.DATAFRAME)
        
        df_risk_factors_data_db = obj_df_risk_factors_data_db.\
                                        getData(\
                                        s_volume="", s_chapter="",\
                                        s_example="", \
                                        s_source=DataSource.db,\
                                        s_source_filename="db_Risk_Factors", \
                                        s_source_type="csv", verbose=False)

        df_risk_factor_type = df_risk_factors_data_db.ix[risk_factor_in]\
                                                        ['Risk Factor Type']
        return df_risk_factor_type
        
            
    def getStockInstrumentBeta_db(self, stock_instrument_id_in):
        
        obj_df_stock_instrument_beta_data_db = DataAsDataFrame(DatasetTypeList.DATAFRAME)
        
        df_stock_instrument_beta_data_db = obj_df_stock_instrument_beta_data_db.\
                                        getData(\
                                        s_volume="", s_chapter="",\
                                        s_example="", \
                                        s_source=DataSource.db,\
                                        s_source_filename="db_Stock_Instruments_Beta", \
                                        s_source_type="csv", verbose=False)

        stock_instrument_beta = df_stock_instrument_beta_data_db.ix[stock_instrument_id_in]\
                                                        ['Beta']
        return stock_instrument_beta
        
class yahoo(object):
    
    def __init__(self):
        LOG_FILENAME = 'example.log'
        logging.basicConfig(filename=LOG_FILENAME,level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        
        self.obj_config = config()
        

#    base_url = "http://ichart.finance.yahoo.com/table.csv?s="
#    def make_url(ticker_symbol):
#        return base_url + ticker_symbol
#    
#    output_path = "C:/path/to/output/directory"
#    def make_filename(ticker_symbol, directory="S&P"):
#        return output_path + "/" + directory + "/" + ticker_symbol + ".csv"
#    
#    def getHistoricalStockPriceData(ticker_symbol, directory="S&P"):
#        try:
#            urllib.urlretrieve(make_url(ticker_symbol), make_filename(ticker_symbol, directory))
#        except urllib.ContentTooShortError as e:
#            outfile = open(make_filename(ticker_symbol, directory), "w")
#            outfile.write(e.content)
#            outfile.close()

    def getHistoricalStockPriceData(self, ticker_symbol_in, start_date_in,\
                                    end_date_in):
                                        
        datetime_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        todays_date = date.today()   # retreived in YYYY-MM-DD format
        n = 7
        date_n_days_ago = date.today() - timedelta(days=n)
        #
        mylist = ['^NYA']
        #
        for yahoo_symbol in mylist:
            try:
                stock_data = web.DataReader(yahoo_symbol, 'yahoo', date_n_days_ago, todays_date)
                print "success in retreiving data for: ",yahoo_symbol
                stock_data.to_csv(self.obj_config.get_yahoo_data_path() + '/' + \
                            yahoo_symbol + '.csv')
            except:
                print "failed in retreiving data for: ",yahoo_symbol