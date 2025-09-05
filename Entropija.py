# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 13:42:55 2019

@author: Matevz
"""

import matplotlib.pyplot as plt
import scipy.integrate as integ
import numpy as np


def funk(x):
    if (6 >= x) and (x <= 8):
        return -(x*x/7)+2*x-7.5
    elif (10 <=x) and (x <= 12):
        return x*x/8 - 2.5 * x + 12.5
    else:
        return 0
    
    
def kumulativa(up):
    return integ.quad(funk,0,up)[0]
    
kumus = []

for i in np.arange(0, 13, 0.1):
    kumus.append(kumulativa(i))
    
plt.plot(kumus)