class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
def copyRandomList(head):
    iter1=head
    while(iter1):
        front1=iter1.next
        newnode=Node(iter1.val)
        iter1.next=newnode
        newnode.next=front1
        iter1=front1
    iter2=head
    while(iter2):
        if iter2.random is not None:
            iter2.next.random=iter2.random.next
        iter2=iter2.next.next
    iter3=Node(0)
    copy=iter3
    iter4=head
        
    while(iter4.next):
        # print(iter3.val)
        front2=iter4.next.next
        iter3.next=iter4.next
        iter4.next=front2
        iter3=iter3.next
    return(copy.next)