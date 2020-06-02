# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        
        """
        prev = ListNode(None)
        if node.next ==  None:
            return
        else:
            
            
            while not(node.next) == None:
                node.val = node.next.val
                prev = node
                node =  node.next
            
            prev.next = None