#python 3


def compare_lists(llist1, llist2):
    nA = llist1
    nB = llist2
    while(nA != None and nB != None):
        if(nA.data != nB.data):
            return 0
        nA = nA.next
        nB = nB.next
    if(nA == None and nB == None):
        return 1
    else:
        return 0