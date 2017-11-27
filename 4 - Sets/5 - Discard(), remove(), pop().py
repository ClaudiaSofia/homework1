n = input()
s = set(map(int, raw_input().split())) 
N = input()

for e in range(N):
    c = raw_input().split()
    command= c[0]
    if command== "pop":
        s.pop()
    elif command== "remove":
        s.remove(int(c[1]))
    elif command == "discard":
        s.discard(int(c[1]))
print (sum(s))