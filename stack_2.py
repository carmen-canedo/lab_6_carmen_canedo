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

    def peak(self):
        return self.top.get_data()

    def pop(self):

        if (self.size > 0):
            print(self.top.get_data())
            prev = self.top
            self.top = self.top.get_next_pointer()
            prev.set_next_pointer(None)
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
