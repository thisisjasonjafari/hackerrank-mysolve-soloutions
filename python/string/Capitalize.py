
def solve(s):
    for x in s.split():
        s = s.replace(x, x.capitalize(), 1) # <--- Using max argument
    return (s)