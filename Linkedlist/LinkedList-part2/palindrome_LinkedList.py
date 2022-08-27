def isPalindrome(head):
    node=head
    sec=head
    st1=[]
    st2=[]
    if head.next==None:
        return True
    while sec!=None and sec.next!=None:
        st1.append(node.val)
        node=node.next
        sec=sec.next.next
        
    while node:
        st2.append(node.val)
        node=node.next
        
    st2.reverse()
    print(st1,st2)
    if len(st1)==len(st2):
        if st1==st2:
            return True
        else:
            return False
    else:
        if st1==st2[:-1]:
            return True
        else:
            return False