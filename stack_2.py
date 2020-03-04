from node import Node

class Stack:
    def __init__(self, top = None, size = 0):
        self.top = top
        self.size = size

    def push(self, new_data):
        # Need to create new node
        new_node = Node(data = new_data)

        # Sets top of stack to the new node
        if (self.top != None):
            new_node.set_next_pointer(self.top)

        self.top = new_node

        # Increases the size of the stack
        self.size += 1

    def peak(self):
        return self.top.get_data()

    def pop(self):

        # Check that the stack isn't empty
        if (self.size > 0):

            # Get the data from the stop
            print(self.top.get_data())

            # Sets temporary variable makes the previous node as the top
            prev = self.top

            # Moving top down to the node below
            self.top = self.top.get_next_pointer()

            # Remove the link from the old node
            prev.set_next_pointer(None)

            # Decrement the size 
            self.size -= 1
        else:
            print("Stack is empty")



def main():

    s = Stack()
    s.push(100)
    s.push("American U")

    print("The size was: ", s.size)
    s.pop()
    print("The size is: ", s.size)

if __name__ == '__main__':
    main()
