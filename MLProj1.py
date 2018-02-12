# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 09:46:06 2018

@author: Emma
"""
import numpy as np
import xlrd
import pandas as pd

# Load xls sheet with data
#dataset = xlrd.open_workbook('wage2.xls').sheet_by_index(0)
#data = pd.get_dummies(dataset)


df = pd.read_excel('wage2.xls', header = None)
n = df.cou
print(n)
#index = list(range(n))
df.columns = ['wage', 'hours', 'iq', 'kww', 'educ', 'exper', 'tenure', 'age', 'married', 'black', 'south', 'urban', 'sibs', 'brthord', 'meduc', 'feduc', 'lwage']
#df.set_index(index, inplace=True)
     
df.dropna(inplace=True)

#print(df.head(12))