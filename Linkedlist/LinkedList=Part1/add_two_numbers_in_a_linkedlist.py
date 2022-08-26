class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
        l3=ListNode(None)
        head=l3
        carry=0
        while(l1!=None or l2!=None):
            if l2==None:
                l2=ListNode(0)
            if l1==None:
                l1=ListNode(0)
            sums=(l1.val+l2.val+carry)%10
            if l3.val is None:
                l3.val=sums
            else:
                
                l3.next=ListNode(sums)
                l3=l3.next
            carry=(l1.val+l2.val+carry)//10
            l1=l1.next
            l2=l2.next
        
        if carry!=0:
            l3.next=ListNode(carry)
        return head