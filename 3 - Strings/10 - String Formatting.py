def print_formatted(number):
    w=len(bin(number)[2:])
    for i in range(1, number+1):
        e = str(i).rjust(w, ' ')
        o= oct(i)[1:].rjust(w, ' ')
        h = hex(i)[2:].upper().rjust(w, ' ')
        b= bin(i)[2:].rjust(w, ' ')
        print e, o, h, b