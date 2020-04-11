
def findMergeNode(headA, headB):
    
    if (headA == None and headB == None):
        return -1
    else:
        currentA = headA
        currentB = headB
        while(currentA != currentB):
            if(currentA.next == None):
                currentA = headB
            else:
                currentA = currentA.next
            if(currentB.next == None):
                currentB = headA
            else:
                currentB = currentB.next
        return currentA.data