# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 08:01:11 2016

@author: yashwantbhambhani
"""

class Base(object):
    def __init__(self, attribute_a_in):
        self.a = attribute_a_in
        
    def getBase(self):
        print self.a
        
class Child(Base):
#    def __init__(self, attribute_b_in):
#        self.b = attribute_b_in
        
    def getBase(self):
        print 'ABC' + self.a
        print self.b