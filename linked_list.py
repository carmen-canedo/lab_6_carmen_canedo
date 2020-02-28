# Lab 6
# Problem 2
#
# Create a LinkedList class
# Attributes:
#   head
#   size
# Create getters and setters
#
# Create these methods:
#   is_empty()
#   add_node()
#   remove_node()

from node import Node

class LinkedList:
    def __init__(self, size = 0, head = None, tail = None):
        self.size = size
        self.head = head
        self.tail = tail

    def get_size(self):
        return self.size

    def set_size(self, new_size):
        self.size = new_size

    def get_head(self):
        return self.head

    def set_head(self, new_head):
        self.head = new_head

    def get_tail(self):
        return self.tail

    def set_tail(self, new_tail):
        self.tail = new_tail

    def is_empty(self, node):
        if (self.get_size() > 0):
            return False 
        return True

    def add_node(self, data):
        size += 1
        new_node = data
        set_next_pointer(new_pointer = tail)
        return

    def remove_node():
        pass
