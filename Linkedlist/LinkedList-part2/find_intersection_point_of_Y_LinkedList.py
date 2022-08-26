def getIntersectionNode(headA,headB):
        dic1={}
        i=0
        while(headA):
            dic1[headA]=i
            i+=1
            headA=headA.next
           
        while(headB):
            if headB in dic1.keys():
                return(headB)
            headB=headB.next