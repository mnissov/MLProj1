#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 15:22:52 2018

@author: morten
"""

from MLProj1 import *


means = np.zeros(7)
for i in range(0,7):
    means[i] = X[:,i].mean()

