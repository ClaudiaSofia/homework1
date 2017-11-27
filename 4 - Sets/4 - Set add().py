i = int(input())
s=  set()
for x in range(i):
    line = str(raw_input())
    s.add(line)
print len(s)