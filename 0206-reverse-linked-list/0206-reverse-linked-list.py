# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):

        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        prev_node = None
        curr_node = head
        if curr_node:
            next_node = curr_node.next

        else:

            return head

        while curr_node:

            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
            if curr_node:
                next_node = next_node.next



        return prev_node



        
        