import numpy as np
 
def normal_dist(x, mean, sd):
    prob_density = 1-(np.pi*sd) * np.exp(-0.5*((x-mean)/sd)**2)
    return prob_density
 
mean = 0
sd = 0.05
x = 0.1
result = normal_dist(x, mean, sd)
print(result)


from math import log2

vrednosti = [0.42, 0.06, 0.01, 0.12, 0.18, 0.02, 0.06, 0.06, 0.07]
info = []
vzaj_entr = 0

for i in vrednosti:
    ent = -log2(i)
    info.append(ent)
    vzaj_entr = vzaj_entr + ent*i

print(info)
print(vzaj_entr)

px = [0.49, 0.32, 0.19]
py = [0.6, 0.3, 0.1]

for i in px:
    print(i*log2(i))
a = 0
for i in py:
    print(i*log2(i))
    a = a + -i*log2(i)

print(a)