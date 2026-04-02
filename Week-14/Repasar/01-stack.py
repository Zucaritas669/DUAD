class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

class Stack:
    def __init__(self,top=None):
        self.top = top
        

    def push(self,data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            print("Stack is empty")
            return
        removed = self.top     
        self.top = self.top.next  
        return removed.data 

    def print_structure(self):
        current_node = self.top
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

        
s = Stack()
s.push("Plato 1")
s.push("Plato 2")
s.push("Plato 3")
s.print_structure()
print("---")
s.pop()
s.print_structure()  



        

        