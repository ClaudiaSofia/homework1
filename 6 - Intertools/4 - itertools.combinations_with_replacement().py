from itertools import combinations_with_replacement
a = raw_input().split()
s= str(a[0])
i= int(a[1])
p = list(combinations_with_replacement(sorted(s),i))

for e in p:
    print("".join(e))