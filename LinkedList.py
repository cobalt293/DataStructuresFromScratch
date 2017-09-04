class Node(object):
    """Node is to be used within the Linked List object"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    
    def __str__(self):
        return 'Node(' + str(self.data) + ', ' + str(self.next) + ')'

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add(self, data):
        """Adds a new Node to the end of the Linked List and returns True 
        when sucessful.  Returns false if something went wrong"""
        # Case 1: list is empty
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
            self.size += 1
            return True
        # Case2: list is not empty
        else:
            tmp = Node(data)
            self.tail.next = tmp
            self.tail = tmp
            self.size += 1
            return True

    def remove(self):
        """Removes the last node in the list and returns the Node object"""

        # Case 1: List has more than one node
        if self.size > 1:
            element_to_remove = self.tail
            cursor = self.head
            while cursor.next is not self.tail:
                cursor = cursor.next
            self.tail = cursor
            self.tail.next = None
            self.size -= 1
            return element_to_remove

        # Case 2: List has 1 Node
        elif self.size == 1:
            element_to_remove = self.head
            self.head = None
            self.tail = None
            return element_to_remove

        # Case 3: List is empty
        else:
            return None
            

    def __str__(self):
        ret = ''
        cursor = self.head
        while cursor is not None:
            ret += str(cursor.data)+" "
            cursor = cursor.next
        return ret

