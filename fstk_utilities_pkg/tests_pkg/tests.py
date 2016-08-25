# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 10:50:46 2016

@author: yashwantbhambhani
"""
import os
import sys

sys.path.append(os.path.abspath('/Users/yashwantbhambhani/Documents/SHWAYB/FSTK'))

from fstk_utilities_pkg.Folder1.SubFolder1.Module1 import cls_module1
from fstk_utilities_pkg.Animals.Mammals import Mammals

obj_folder1_module1 = cls_module1()
obj_folder1_module1.fn_cls_module1()

obj_AnimalsFolder_MammalsModule = Mammals()
obj_AnimalsFolder_MammalsModule.printMembers()
