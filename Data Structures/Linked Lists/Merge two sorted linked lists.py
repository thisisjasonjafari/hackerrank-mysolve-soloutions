
def mergeLists(headA, headB):
    
    if(headA == None and headB == None):
        return None
    elif(headA == None):
        return headB
    elif(headB == None):
        return headA
    elif(headA.data <= headB.data):
        headA.next = mergeLists(headA.next, headB)
        return headA
    else:
        headB.next = mergeLists(headA, headB.next)
        return headB