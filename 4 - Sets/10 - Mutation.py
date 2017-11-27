n = input()
A = set(map(int, raw_input().split()))
N = input()
for _ in xrange(N):
    c = raw_input().split()
    S = set(map(int, raw_input().split()))
    com = str(c[0])
    getattr(A, com)(S)
    
print str(sum(A))