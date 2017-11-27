import string
alpha = string.ascii_lowercase

def print_rangoli(n):
    l = []
    for i in range(n):
        s = "-".join(alpha[i:n])
        l.append(s[::-1]+s[1:])
    width = len(l[0])

    for i in range(n-1, 0, -1):
        print(l[i].center(width, "-"))

    for i in range(n):
        print(l[i].center(width, "-"))