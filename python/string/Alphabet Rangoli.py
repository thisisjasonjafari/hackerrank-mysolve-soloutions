import string

def print_rangoli(size):
    
    alpha = string.ascii_lowercase
    n = size
    L = []
    for i in range(n):
        s = "-".join(alpha[i:n])
        L.append((s[::-1]+s[1:]).center(4*n-3, "-"))
    print('\n'.join(L[:0:-1]+L))
        # your code goes here