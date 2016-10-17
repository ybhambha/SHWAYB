# -*- coding: utf-8 -*-
import logging
import numpy as np
import math

class array_util(object):
    def __init__(self):
        LOG_FILENAME = 'example.log'
        logging.basicConfig(filename=LOG_FILENAME,level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        
    def calc_var_covar_matrix(self, items_in, df_std_dev_items_in, \
                                    corr_items_in):
                                
        cm = np.array(corr_items_in)
        items = items_in
        df_std_dev_items = df_std_dev_items_in
        print df_std_dev_items
        
        arr_var_covar = []
        
        for each_item in items:
            row_var_covar = []
            for item_id in items:
                if each_item == item_id:
                    variance = math.pow(df_std_dev_items.ix[item_id][0],2)
                    row_var_covar.append(variance)
                else:
                    cov = df_std_dev_items.ix[item_id][0]\
                            *df_std_dev_items.ix[each_item][0]\
                            *cm[items.index(item_id)][items.index(each_item)]
                    row_var_covar.append(cov)
            arr_var_covar.append(row_var_covar)
    
        mat_var_covar = np.mat(arr_var_covar)
    
        return mat_var_covar