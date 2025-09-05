# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from math import log

def f(x):
    a = 0.8 * x * log((0.8/(0.2 + 0.6 * x )),2)
    b = 0-2 * x * log((0.2/(0.8-0.6*x)),2)
    c = 0.2*(1-x)*log((0.2/(0.2+0.6*x)),2)
    d = 0.8*(1-x)*log((0.8/(0.8-0.6*x)),2)
    return (a+b+c+d)