def mutate_string(string, position, character):
    b=""
    for i in range(len(string)):
        if (i ) == position :
            b = b + character
        else:
            b = b + string[i]
    return b