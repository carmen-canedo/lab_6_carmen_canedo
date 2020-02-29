# Lab 6
# Problem 2

# Importing Node class from node.py
from node import Node

# Creating LinkedList class
class LinkedList:

    # Initializing attributes for LinkedList
    def __init__(self, size = 0, head = None, tail = None):
        self.size = size
        self.head = head
        self.tail = tail

    # Defining getter and setter methods for each attribute
    # Methods for size attributes
    def get_size(self):
        return self.size

    def set_size(self, new_size):
        self.size = new_size

    # Methods for head attribute
    def get_head(self):
        return self.head

    def set_head(self, new_head):
        self.head = new_head

    # Methods for tail attribute
    def get_tail(self):
        return self.tail

    def set_tail(self, new_tail):
        self.tail = new_tail

    # Methods for list
    # Checks if list is empty
    def is_empty(self):
        if (self.get_size() > 0):
            return False
        return True

    # Adds node to list
    def add_node(self, new_data):
        new_node = Node(data = new_data)

        # Simple Case
        if (self.is_empty() == True):
            self.set_head(new_node)
        else:
            t = self.get_tail()
            t.set_next_pointer(new_node)

        self.set_tail(new_node)
        self.set_size(self.size + 1)

def main():

    ll = LinkedList()
    ll.add_node(new_data = 1000)
    print(ll.get_size())

    print(ll.get_tail().get_data())

if __name__ == '__main__':
    main()
