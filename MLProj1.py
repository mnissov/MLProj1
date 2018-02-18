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


df = pd.read_excel('modified.xls', header = None)
n = len(df.index)
#print(n)
#index = list(range(n))
#df.columns = ['wage', 'hours', 'iq', 'educ', 'exper', 'tenure', 'age', 'black']
df.reset_index()
df.reindex(index=range(0,n))
     
df.dropna(inplace=True)
dfMatrix = df.as_matrix()

#print(dfMatrix)

y = dfMatrix[1:,0]
yMatrix = np.mat(y)

X = np.mat(np.empty((n,7))
for i in range(7):
    X[i,:] = np.matrix(dfMatrix[)