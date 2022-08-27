def removeNthFromEnd(head,n):
        temp=head
        temp2=head
        if temp.next==None:
            head=None
            return head
        for i in range(n):
            if temp is None:
                return None
            temp=temp.next
        if temp:
            while temp.next:
                temp = temp.next
                temp2 = temp2.next
            temp2.next=temp2.next.next
            return head
        
        elif temp is None:
            return head.next
        else:
            head.next=None
            return head