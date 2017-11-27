from itertools import permutations
a = raw_input().split()
s= str(a[0])
i= int(a[1])
p = list(permutations(sorted(s),i))

for e in p:
    print("".join(e))