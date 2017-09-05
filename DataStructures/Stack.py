class Node(object):
    """Node is to be used within the Linked List object"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Stack(object):
    def __init__(self):
        self.head = None
        self.size = 0

    def empty(self):
        """Tests if this stack is empty."""
        if self.size == 0:
            return True
        else:
            return False
    
    def peek(self):
        """Looks at the object at the top of this stack without removing it from the stack."""
        

    def pop(self):
        """Removes the object at the top of this stack and returns that object as the value of this function."""

    def push(self):
        """Pushes an item onto the top of this stack."""

    def search(self,Node):
        """Returns the 1-based position where an object is on this stack."""