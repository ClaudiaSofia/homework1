def merge_the_tools(string, k):
    n = len(string)
    p = n/k #how many lines
    l = []
    for e in range(p):
        ss= string[e*k:(e*k)+k] #substrings of lenght k
        l.append(ss)
    for i in l:
        np= "" #without repitition
        for c in i:
            if c not in np:
                np += c
        print np
        