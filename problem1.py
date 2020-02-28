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

    def get_data(self, new_data):
        return self.data = new_data

    def set_data(self):
        return self.data
