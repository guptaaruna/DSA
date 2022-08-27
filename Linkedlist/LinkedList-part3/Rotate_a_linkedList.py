def rotateRight(head):
    if k==0 or head==None or head.next==None:
        return(head)
    first=head
    temp=first.val
    c=0
    while(first):
        first=first.next
        c+=1
            
    first=head
    k=k%c
    for i in range(k):
        while(first):
            if first.next:
                temp1=first.next.val
                (first.next.val,temp)=(temp,first.next.val)
            temp=temp1
            first=first.next
        first=head
        head.val=temp
    return(head)