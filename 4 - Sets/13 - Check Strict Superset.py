A = set(map(int, raw_input().split()))
n = int(input())
sup= []
for i in range(n):   
    B = set(map(int, raw_input().split()))
    sup.append(A.issuperset(B))
print all(sup)