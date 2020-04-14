
def isMotagharen(n):
    if len(n) == 6:
        if n[0] == n[5] and n[1] == n[4] and n[2] == n[3]:
            return True
    else:
        return False
    

for i in range(900,999):
    for b in range(900,999):
        if isMotagharen(str(i * b)) == True:
            la = i
            lb = b
                
            
print("For numbers: " + str(la) + " and " + str(lb))
print("You have answer: " + str(la*lb))
