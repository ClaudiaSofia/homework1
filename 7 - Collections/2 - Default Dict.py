from collections import defaultdict
d = defaultdict(list)

nm = list(map(int, raw_input().split()))
n = nm[0]
m = nm[1]
for i in range(n):
    d[raw_input()].append(i + 1)

for i in range(m):
    print(' '.join(map(str, d[raw_input()])) or -1)