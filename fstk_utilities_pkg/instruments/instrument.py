# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 08:11:18 2016

@author: yashwantbhambhani
"""
import pandas as pd
import logging

from fstk_utilities_pkg.risk_manager.equity_risk import equity_risk_model
from fstk_utilities_pkg.instruments.derivative import *
from fstk_utilities_pkg.data_access_utilities.data_access_util import *
from fstk_utilities_pkg.instruments.instrument import *

class InstrumentType(object):
    EQT= "Equity"
    FI = "Fixed Income"
    DERV = "DERIVATIVE"
    COM = "Commodity"