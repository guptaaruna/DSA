class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):
        if list1 is None and list2 is None:
            return list1
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        head1=list1
        # print(head1.next.val)
        head2=list2
        while (head1!=None and head2!=None):
            
            if head1.val<head2.val:
                if head1.next==None:
                    head1.next=head2
                    head1=None
                else:
                    head1=head1.next  
            elif head1.val==head2.val:
                temp=head1.next
                head1.next=ListNode(head2.val)
                head1.next.next=temp
                head1=head1.next
                head2=head2.next    
            elif head1.val>head2.val:
                (head1.val,head2.val)=(head2.val,head1.val)
                temp=head1.next
                head1.next=ListNode(head2.val)
                head1.next.next=temp
                head1=head1.next
                head2=head2.next
        
        return list1