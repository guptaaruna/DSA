def hasCycle(head):
    dic={}
    i=0
    while(head):
        if head in dic:
            return True
        dic[head]=i
        i+=1
        head=head.next
    return False