
def removeDuplicates(head):
    
    n = head
    while (n.next != None):
        if(n.data==n.next.data):
            t = n.next
            n.next= t.next
        else:
            n = n.next
    return head