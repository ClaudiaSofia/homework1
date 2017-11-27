#too slow
from collections import OrderedDict
n = int(input())
w= OrderedDict()
for e in range(n):
    a= raw_input()
    if a not in w.keys():
        w.update({a : 1})
    else:
        w[a] +=1
print len(w)

for i in (w.values()):
    print i,