def wrap(string, max_width):
    r = len(string)/max_width
    for e in range(r):
        g = e*max_width
        c = string[g:(g+max_width)]
        print c
    if r*max_width != len(string):
        d = r*max_width
        return string[d:]
    