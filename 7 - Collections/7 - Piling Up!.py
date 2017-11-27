T = int(input())
for t in range(T):
    n = int(input())
    c = list(map(int, raw_input().split()))
    m = min(c)
    mi = c.index(m)
    left= c[:mi]
    right= c[mi+1:]
    if left==sorted(left, reverse= True) and right== sorted(right):
        print ('Yes')
    else: 
        print('No')