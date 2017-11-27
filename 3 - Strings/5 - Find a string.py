def count_substring(string, sub_string):
    c = 0
    lens= len(string)
    lenss =len(sub_string)
    for e in range(lens):
        if string[e] == sub_string[0]:
            if string[e:e + lenss] == sub_string:
                c +=  1
    return c