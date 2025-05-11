class Node:

    def __init__(self, data, next = None):

        self.data = data
        self.next = next



class MyLinkedList(object):

    def __init__(self):

        self.head = None

        self.len = 0

        

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """

        if self.len <= index or index < 0:

            return -1

        curr = self.head

        for _ in range(index):

            curr = curr.next

        return curr.data

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        self.len+=1
        

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """

        new_node = Node(val)

        if not self.head:

            self.head = new_node

        else:

            curr = self.head

            while curr.next:

                curr = curr.next

            curr.next = new_node

        self.len+=1
        

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """

        if index > self.len:
            return

        if index == self.len:

            self.addAtTail(val)

        elif index == 0:

            self.addAtHead(val)
        
        else:

            new_node = Node(val)

            curr = self.head

            for _ in range(index-1):

                curr = curr.next

            new_node.next = curr.next
            curr.next = new_node

            self.len += 1
        

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """

        if index >= self.len:

            return

        if index == 0:

            self.head = self.head.next

        else:

            curr = self.head 

            for _ in range(index-1):
                curr = curr.next

            curr.next = curr.next.next

        self.len -= 1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)