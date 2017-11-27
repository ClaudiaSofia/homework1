from itertools import product
km = raw_input().split()
K = int(km[0])
M = int(km[1])
l = []
for i in range(K):
    l.append(map(lambda x: int(x)**2, raw_input().split()[1:]))
    
t = max(product(*l), key = lambda x: sum(x)%M)
print sum(t)%M 