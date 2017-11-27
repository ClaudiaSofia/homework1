from itertools import combinations
N = int(input())
L = raw_input().split()
K = int(input())
c = list(combinations(L,K))
r =  [i for i in c if 'a' in i]       
print (len(r)/float(len(c)))