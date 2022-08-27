def middleNode(head):
        ptr1=head
        ptr2=head
# method1:
#         while((ptr2 is not None) and (ptr2.next is not None)):
#             ptr1=ptr1.next
#             ptr2=ptr2.next.next
            
#         return ptr1
# method2:
        c=0
        while(ptr1):
            c+=1
            ptr1=ptr1.next
        c=c//2
        for i in range(c):
            ptr2=ptr2.next
        return(ptr2)