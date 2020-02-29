# Lab 6
# Problem 1

# Creating class Node
class Node:

    # Initializing attributes for Node
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


def main():

    # Setting node cargo to 100
    n = Node(data = 100)

    # Printing the value of n using get_data method
    print(n.get_data())

    # Changing data in node
    n.set_data("AU")

    # Printing new results
    print(n.get_data())


if __name__ == '__main__':
    main()
