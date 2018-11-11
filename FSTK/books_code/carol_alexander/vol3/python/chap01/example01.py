# -*- coding: utf-8 -*-
#Example III.1.1: Continuous Versus Discrete Compounding
import sys
import os

sys.path.append(os.path.abspath('/Users/yashwantbhambhani/Documents/SHWAYB/FSTK'))
from fstk_utilities_pkg.common_utilities.InterestRate import *

#Inputs
Principal = 500
Maturity = 3.5
Rate = 0.04
Freq = InterestAccrualFrequency.SA #Semi-annual for discrete compounding

#Calculations
objDiscretelyCompoundedSpotRate = DiscretelyCompoundedSpotRate(Rate, Maturity, Freq)
objContinuouslyCompoundedSpotRate = ContinuouslyCompoundedSpotRate(Rate, Maturity)

#Output
print "Future Value using discrete compounding: " + \
            str(objDiscretelyCompoundedSpotRate.FutureValue(500))
print "Future Value using continuous compounding: " + \
            str(objContinuouslyCompoundedSpotRate.FutureValue(500))
            