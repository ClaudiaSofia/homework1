from collections import Counter
#!/bin/python
import sys
if __name__ == "__main__":
    s = raw_input().strip()
    c = Counter(s)
    cs = sorted(c.items(), key= lambda x: (-x[1],x[0]))[:3]
    for e in cs:
        print e[0], e[1]