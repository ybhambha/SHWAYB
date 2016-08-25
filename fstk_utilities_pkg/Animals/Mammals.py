# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 13:31:45 2016

@author: yashwantbhambhani
"""

class Mammals:
    def __init__(self):
        ''' Constructor for this class. '''
        # Create some member animals
        self.members = ['Tiger', 'Elephant', 'Wild Cat']
        
    def printMembers(self):
        print('Printing members of the Mammals class')
        for member in self.members:
            print('\t%s ' % member)