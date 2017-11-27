from collections import Counter
X= int(input())
x = list(map(int, raw_input().split()))
N = int(input())

money = 0
for e in range(0, N):
    size, prize= list(map(int, raw_input().split()))
    if size in x:
        money+= prize
        x.remove(size)
print money