def swap_case(s):
    swap = ""
    for letter in s:
        if letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            low= letter.lower()
            swap += low
        elif letter in "abcdefghijklmnopqrstuvwxyz":
            up= letter.upper()
            swap += up
        else: swap += letter
            
    return swap