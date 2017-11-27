def mutate_string(string, position, character):
    ls= list(string)
    ls[position] = character
    ns = "".join(ls)
    return ns