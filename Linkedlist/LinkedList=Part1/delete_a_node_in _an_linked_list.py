def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        while node.next:
            prev=node
            node.val=node.next.val
            node=node.next
        prev.next=None