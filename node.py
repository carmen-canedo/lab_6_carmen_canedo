# Lab 6
# Problem 1 and 2

# Creating class Node
class Node:

    # Initializing attributes for node
    def __init__(self, data, next_pointer = None):
        self.data = data
        self.next_pointer = next_pointer

    # Defining getter and setter methods
    # Returns current data (Getter)
    def get_data(self):
        return self.data

    # Modifies data in node (Setter)
    def set_data(self, new_data):
        self.data = new_data

    # Returns the next pointer
    def get_next_pointer(self):
        return self.next_pointer

    # Modifies a new pointer
    def set_next_pointer(self, new_pointer):
        self.next_pointer = new_pointer

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

def main():

    n = Node(data = 100)

    print(n.get_data())

    n.set_data("AU")

    print(n.get_data())


if __name__ == '__main__':
    main()
