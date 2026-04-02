class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class Deque:
    def __init__(self):
        self.head = None
        self.tail = None

    def push_right(self, data):
        new_node = Node(data)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def push_left(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def pop_right(self):
        if self.tail is None:
            print("Deque is empty")
            return
        removed = self.tail
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        else:
            self.head = None
        return removed.data

    def pop_left(self):
        if self.head is None:
            print("Deque is empty")
            return
        removed = self.head
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        return removed.data

    def print_structure(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next


d = Deque()
d.push_right("A")
d.push_right("B")
d.push_left("Z")
d.print_structure()
print("---")
d.pop_right()
d.print_structure()