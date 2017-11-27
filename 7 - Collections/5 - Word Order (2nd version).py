from __future__ import print_function #for use print like in python 3, but always slow
from collections import OrderedDict

n = int(input())
w= OrderedDict()
for e in range(n):
    a= raw_input()
    if a not in w.keys():
        w[a] = 1
    else:
        w[a] +=1
print (len(w))
v = w.values()
print (*v, sep=" ")