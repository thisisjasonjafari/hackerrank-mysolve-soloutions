def merge_the_tools(string, k):
    S = string
    N = k
    temp = []
    len_temp = 0
    for item in S:
        len_temp += 1
        if item not in temp:
            temp.append(item)
        if len_temp == k:
            print ''.join(temp)
            temp = []
            len_temp = 0