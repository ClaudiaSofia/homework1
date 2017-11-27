#not for too long words

def all_consecutive_substrings(string):
    s = tuple(string)
    for size in range(1, len(s)+1):
        for index in range(len(s)+1-size):
            yield string[index:index+size]

def minion_game(string):
    subs = list(all_consecutive_substrings(string))
    K = 0
    S = 0
    for e in subs:
        if e[0] in "AEIOU":
            K += 1
        else:
            S +=1
    l  = [["Kevin", K], ["Stuart", S]]
    if K == S:
        print "Draw"
    else: 
        l.sort(key=lambda x: x[1], reverse= True)
        print l[0][0] + " " + str(l[0][1])
        
    