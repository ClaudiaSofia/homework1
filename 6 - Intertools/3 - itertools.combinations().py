from itertools import combinations
a = raw_input().split()
s= str(a[0])
i= int(a[1])
p = []
for n in range(1,i+1):
    p += list(combinations(sorted(s),n))

for e in p:
    print("".join(e))