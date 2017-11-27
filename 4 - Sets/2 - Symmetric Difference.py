a = input()
aa= set(map(int, raw_input().split()))
b= input()
bb= set(map(int, raw_input().split()))

s =(aa).symmetric_difference(bb)
l = list(s)
l.sort()
for e in l:
    print e