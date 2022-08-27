class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None
def flatten(root):
    def merge(a,b):
        temp=Node(0)
        res=temp
        while(a!=None and b!=None):
            if(a.data<b.data):
                temp.bottom=a
                temp=temp.bottom
                a=a.bottom
            else:
                temp.bottom=b
                temp=temp.bottom
                b=b.bottom
                
            if(a!=None):
                temp.bottom=a
            else:
                temp.bottom=b
        return(res.bottom)
        
    if (root.next is None) or (root is None):
        return root
    else:
        root.next=flatten(root.next)
        root=merge(root,root.next)
    return root
