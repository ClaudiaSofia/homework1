if __name__ == '__main__':
    N = int(input())
    l = []
    for _ in range(N):
        c = raw_input().split()
        command = c[0]
        args = c[1:]
        if command != "print":
            command += "("+ ",".join(args) +")"
            eval("l."+command)
        else:
            print l