# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 08:31:01 2019

@author: matev
"""

import cmath
import math

zk = complex(50,0)
zl = complex(100,100)

offset = - math.pi

gamma = (zl-zk)/(zl+zk)
print(gamma)
gama = list(cmath.polar(gamma))
gama[1] += offset

gamma = cmath.rect(gama[0],gama[1])

zl = zk * (1 - gamma)/(1 + gamma)

print(zl)



