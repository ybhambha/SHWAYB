# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 13:33:15 2016

@author: yashwantbhambhani
"""

class Birds:
    def __init__(self):
        ''' Constructor for this class. '''
        # Create some member animals
        self.members = ['Sparrow', 'Robin', 'Duck']
 
 
    def printMembers(self):
        print('Printing members of the Birds class')
        for member in self.members:
           print('\t%s ' % member)