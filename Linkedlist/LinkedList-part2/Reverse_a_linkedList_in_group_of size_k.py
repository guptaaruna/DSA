class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseKGroup(head, k):
        dummy=ListNode(0)
        dummy.next=head
        pre=dummy
        cur=dummy
        nex=dummy
        count=0
        while(cur.next):
            cur=cur.next
            count+=1
        while(count>=k):
            cur=pre.next
            nex=cur.next
            i=1
            while(i<k):
                # print(cur.val)
                cur.next=nex.next
                nex.next=pre.next
                pre.next=nex
                nex=cur.next
                i+=1
            pre=cur
            count-=k
        return(dummy.next)