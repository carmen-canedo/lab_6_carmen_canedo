from node import Node

class Stack:
    def __init__(self, top = None, size = 0):
        self.top = top
        self.size = size

    def push(self, new_data):
        new_node = Node(data = new_data)

        if (self.top != None):
            new_node.set_next_pointer(self.top)

        self.top = new_node
        self.size += 1

def main():

    s = Stack()

if __name__ == '__main__':
    main()
