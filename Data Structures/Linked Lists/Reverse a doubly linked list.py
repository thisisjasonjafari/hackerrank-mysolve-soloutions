def reverse(head):
    temp = None
    current = head
    
    while (current != None):
        temp = current.prev
        current.prev = current.next
        current.next = temp
        current = current.prev
        
    if (temp != None):
       head = temp.prev
    return head
 