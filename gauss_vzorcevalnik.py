# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 15:17:40 2023

@author: Matevz
"""

# import required libraries
from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
from math import sqrt

 
# Creating the distribution
#data = np.arange(1,10,0.01)
#pdf = norm.pdf(data , loc = 5.3 , scale = 1 )
 
#loc = povprečna vrednost šuma
#scale = !!koren variance

#Probability of height to be under 4.5 ft.
prob_1 = norm(loc = 0.25 , scale = sqrt(1)).cdf(-1)
print(prob_1)
 
#probability that the height of the person will be between 6.5 and 4.5 ft.
 
cdf_upper_limit = norm(loc = 0.25 , scale = sqrt(1)).cdf(-1)
cdf_lower_limit = norm(loc = 0.25 , scale = sqrt(1)).cdf(0)
 
prob_2 = cdf_upper_limit - cdf_lower_limit
print(prob_2)
 
#probability that the height of a person chosen randomly will be above 6.5ft
 
cdf_value = norm(loc = 5.3 , scale = 1).cdf(6.5)
prob_3 = 1- cdf_value
print(prob_3)

## loc = povprečna vrednost šuma, scale = efektivna vrednost, cdf = vrednost ki jo mora doseči šum

efekt_vr = 0.1
pov_vred = 0.0
input_levels = [-0.4,-0.2,0.2,0.4] # nivoji ki jih pošiljamo
konverter_treshold = [-0.3,0,0.3] # meje intervalov
intervali = []


for x in input_levels:
    count = 0;
    temp = [-9999]
    for y in konverter_treshold:
        if y > x:
            temp.append(y-x)
        else:
            temp.append(-(x-y))
    temp.append(9999)  
    intervali.append(temp)      
        
print(intervali)        
