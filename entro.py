# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 19:15:16 2021

@author: Matevz
"""

import collections
import string
from math import log2
from collections import OrderedDict
import matplotlib.pyplot as plt

def count_letters(text_file, case_sensitive=False):
    with open(text_file, 'r') as f:
        original_text = f.read()
    if case_sensitive:
        alphabet = string.ascii_letters
        text = original_text
    else:
        alphabet = string.ascii_lowercase
        text = original_text.lower()
        alphabet_set = set(alphabet)
        counts = collections.Counter(c for c in text if c in alphabet_set)

    for letter in alphabet:
        print(letter, counts[letter])

    print("total:", sum(counts.values()))

    return counts

rez = OrderedDict(sorted(count_letters("story.txt").items(), key=lambda t: t[0]))
N = sum(rez.values())
info = {}
H = 0

plt.figure()
plt.bar(rez.keys(),rez.values(),width=0.8,color='g')



rez = {key :  value/N for key,value in rez.items()}
info = {key : -log2(rez[key]+1e-100) for key in rez.keys()}


for k in rez.keys():
    H += rez[k]*info[k]
   

print("Max entropija ", log2(25))

plt.figure()    
plt.bar(rez.keys(),rez.values(),width=0.8,color='g')
print("Entropija teksta je ",H)
plt.show()


    

    

