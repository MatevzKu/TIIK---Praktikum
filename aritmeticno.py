# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 10:49:20 2021

@author: Matevz
"""

# x1, x2, x3, x4, x5, xend

verjetnosti = [3/10,4/10,2/10,1/10]
zaporedje = [2,3,2,3,1,4]

start = 0.0
stop = 1.0
reverse = False

print(len(verjetnosti))
if reverse:
    verjetnosti.reverse()
inte = [start,stop]
new_int = [];
output = ""
for j in zaporedje:
    new_int = [];
    for i in range(len(verjetnosti)):
        razpon = (inte[1] - inte[0])/100
        
        #print(i)
        if i == 0:
            temp = [inte[0],inte[0] + razpon*verjetnosti[i]*100]
            new_int.append(temp)
            next_b = temp[1];
        elif i == (len(verjetnosti)-1):
            temp = [next_b,inte[1]]
            new_int.append(temp)
        else:
            temp = [next_b,next_b + razpon*verjetnosti[i]*100]
            new_int.append(temp)
            next_b = temp[1]
    #print(new_int)
    if not reverse:
        inte = new_int[j-1]
    else:
        inte = new_int[len(verjetnosti)-j]
    #print(inte)
    output += f"Trenutni člen je {j}  interval pa je {inte[0]:.5f}------{inte[1]:.5f}\n"


print(output)
output = ""

for zap in zaporedje:
    razpon = (stop - start)/100  #normirano na en procent
    ##print("razpon",razpon)
    stop = start
    for i in range(zap-1):
        stop = stop + razpon*verjetnosti[i]*100;
        ##print("offset",razpon*verjetnosti[i]*100);
        start = start + razpon*verjetnosti[i]*100;
    if zap > 1:
        stop = stop + razpon*verjetnosti[i+1]*100;
    else:
        stop = stop + razpon*verjetnosti[0]*100;
    #print("ternutni clen:",zap)
    #print("konec :",stop)
    #print("start :",start)
    #print(f"Trenutni člen je {zap}  interval pa je {start:.5f}------{stop:.5f}")
    output += f"Trenutni člen je {zap}  interval pa je {start:.5f}------{stop:.5f}\n"

print(output)
    
    