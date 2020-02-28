# Lab 6
# Problem 1
#
# Create a node class
#   Attributes:
#       data
#       next
#  Should have getters and setters
#

class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

    def get_data(self):
        return self.data

    def set_data(self, new_data):
        self.data = new_data

class LinkedList:
    def __init__(self, head = None, size = 0):
        self.head = head
        self.size = size

    def is_empty():
        pass

    def add_node():
        pass

    def remove_node():
        pass 
