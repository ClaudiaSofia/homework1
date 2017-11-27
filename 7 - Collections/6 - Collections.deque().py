from collections import deque
d = deque()
N = int(input())
for _ in range(N):
    c = raw_input().split()
    command = c[0]
    args = c[1:]
    command += "("+ ",".join(args) +")"
    eval("d."+command)

for e in d:
    print e,