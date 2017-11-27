nm = list(map(int, raw_input().split()))
array = list(map(int, raw_input().split()))
A = set(map(int, raw_input().split()))
B = set(map(int, raw_input().split()))
a= 0 
for e in array:
    if e in A:
        a +=1
    if e in B:
        a += -1
print a