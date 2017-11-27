from itertools import product
a = list(map(int, raw_input().split()))
b = list(map(int, raw_input().split()))
AxB =list(product(a,b))

print " ".join(map(str,AxB))