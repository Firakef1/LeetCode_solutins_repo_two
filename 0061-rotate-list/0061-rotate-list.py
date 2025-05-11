# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        counter = 0
        curr = head
        node_vals = []
        while curr:
            node_vals.append(curr.val)
            curr = curr.next
            counter += 1   

        if k == 0 or counter == 0:

            return head

        steps = k%counter

        node_vals = node_vals[-steps:] + node_vals[0:-steps]

        curr = head
        curr.val = node_vals[0]
        for i in range(1, counter):
            curr = curr.next

            curr.val = node_vals[i]


        return head

        
        