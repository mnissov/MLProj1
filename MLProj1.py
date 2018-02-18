# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 09:46:06 2018

@author: Emma
"""
import numpy as np
import xlrd
import pandas as pd
import math

from matplotlib.pyplot import figure, plot, title, xlabel, ylabel, show
from scipy.linalg import svd

# Load xls sheet with data
#dataset = xlrd.open_workbook('wage2.xls').sheet_by_index(0)
#data = pd.get_dummies(dataset)


df = pd.read_excel('modified.xls', header = None)
doc = xlrd.open_workbook('modified.xls').sheet_by_index(0)

attributeNames = doc.row_values(0, 1, 8)
n = len(df.index)
df.reset_index()
df.reindex(index=range(0,n))
     
df.dropna(inplace=True)
dfMatrix = df.as_matrix()

y = dfMatrix[1:,0]
yMatrix = np.mat(y)

X = np.mat(np.empty((n-1,7)))

for i, col_id in enumerate(range(1,8)):
    X[:,i] = np.matrix(doc.col_values(col_id, 1, n)).T
    
N = len(y)
M = len(attributeNames)

# Subtract mean value from data
Y = X - np.ones((N,1))*X.mean(0)

# PCA by computing SVD of Y
U,S,V = svd(Y,full_matrices=False)

# Compute variance explained by principal components
rho = (S*S) / (S*S).sum() 

# Plot variance explained
figure()
plot(range(1,len(rho)+1),rho,'o-')
title('Variance explained by principal components');
xlabel('Principal component');
ylabel('Variance explained');
show()


plot(X, y, 'o')
title('Wage vs Attributres')
xlabel('Attributes')
ylabel('Wage')
legend(attributeNames, loc=4)
show()

