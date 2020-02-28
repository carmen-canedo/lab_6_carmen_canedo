# Lab 6
# Problem 1 and 2

# Creating class Node
class Node:

    # Initializing attributes
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

    # Gets
    def get_data(self):
        return self.data

    def set_data(self, new_data):
        self.data = new_data

class LinkedList:
    def __init__(self, head = None, size = 0):
        self.head = head
        self.size = size

    def is_empty(node):
        if node is None:
            print("This node is empty.")

    def add_node():
        pass

    def remove_node():
        pass
