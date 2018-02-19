#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 15:22:52 2018

@author: morten
"""

from MLProj1 import *
from similarity import similarity


means = np.zeros(7)
median = np.median(X, axis=0)
sd = np.zeros(7)
maxes = np.zeros(7)
mins = np.zeros(7)
var = np.var(X,axis=0)
sim1 = np.zeros(7)

for i in range(0,7):
    means[i] = X[:,i].mean()
    sd[i] = X[:,i].std(ddof=1)
    maxes[i] = X[:,i].max()
    mins[i] = X[:,i].min()
    
myvar=np.zeros(7)
for j in range (0,7):
    for i in range(0,934):
        myvar[j] += ((X[i,j]-means[j]) ** 2)/934
        
cov = np.zeros((7,7))
for i in range (0,7):
    for j in range(0,7):
        for k in range(0,934):
            cov[i,j] += ((X[k,i]-means[i]) * (X[k,j] - means[j]))/935