def has_cycle(head):
    
    fast = head
    slow = head
    while(fast != None and fast.next != None):
        fast = fast.next.next
        slow = slow.next
        if(slow == fast):
            return True
    return False
    