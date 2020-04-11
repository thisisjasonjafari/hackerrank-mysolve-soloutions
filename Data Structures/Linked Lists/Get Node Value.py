
def getNode(head, position):
    
    p = head
    list = []
    list.append(p.data)
    while(p.next!= None):
        p = p.next
        list.append(p.data)
    return list[len(list)-position-1]