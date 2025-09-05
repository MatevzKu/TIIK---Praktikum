# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 13:56:12 2019

@author: Matevz
"""

import numpy as np
from math import log2


#matrika = np.array([[0.2 , 0.02 , 0.05],[0.05, 0.3, 0.07],[0.03, 0.08, 0.2]])

#p_x = [sum(matrika[:,0]),sum(matrika[:,1]),sum(matrika[:,2])]
#p_y = [sum(matrika[0,:]),sum(matrika[1,:]),sum(matrika[2,:])]

#test = True


testko = np.ones([4,4])/16

count = 0
#print(testko)


while count < 20:

    row = np.random.randint(testko.shape[0])
    col = np.random.randint(testko.shape[1])
    wid = testko.shape[0]-1
    hei = testko.shape[1]-1
    a_row = wid-row
    a_col = hei-col
    
    change = round(np.random.rand(),2)
    
    if ((testko[row][col]+change) <= 1) and ((testko[a_row][a_col]-change) >= 0):
        testko[row][col] += change

        testko[a_row][a_col] -= change
        count += 1

print(testko)
testko = np.array([[0.39,0.06,0.01],[0.15,0.19,0.02],[0.04,0.05,0.09]])



print(testko)

p_x = [sum(testko[0]),sum(testko[1]),sum(testko[2])]
p_y = [sum(testko[:,0]),sum(testko[:,1]),sum(testko[:,2])]

print(p_x)
print(sum(p_x))
print(p_y)
print(sum(p_y))


h_x = 0
h_y = 0

for i in p_x:
    h_x = h_x - i*log2(i)

for i in p_y:
    h_y = h_y - i*log2(i)

print(h_x)
print(h_y)


"""
[[0.1025 0.1125 0.1125 0.0525]
 [0.0825 0.0725 0.0825 0.0625]
 [0.0625 0.0425 0.0525 0.0425]
 [0.0725 0.0125 0.0125 0.0225]]
[0.38, 0.3, 0.2, 0.12000000000000001]
0.9999999999999999
[0.32, 0.23999999999999996, 0.26, 0.18]
1.0
"""


