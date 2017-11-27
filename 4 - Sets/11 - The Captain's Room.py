K = input()
L = list(map(int, raw_input().split()))
S = set(L) 
ls = sum(L)
ss = sum(S)*K
print ((ss-ls)/(K-1))