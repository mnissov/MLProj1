# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 09:46:06 2018

@author: Emma
"""
import numpy as np
import xlrd
import pandas as pd

# Load xls sheet with data
dataset = xlrd.open_workbook('wage2.xls').sheet_by_index(0)
data = pd.get_dummies(dataset)

dataframe = pd.read_excel('wage2.xls', header = None)
df
