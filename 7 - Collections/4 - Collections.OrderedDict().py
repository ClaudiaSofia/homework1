from collections import OrderedDict
l= OrderedDict()
N = int(input())
for i in range(N):
    line = raw_input().split()
    item, price = ' '.join(line[:-1]), int(line[-1])
    l[item] = l.get(item, 0) + int(price)
for item, price in l.items():
    print(" ".join([item, str(price)]))