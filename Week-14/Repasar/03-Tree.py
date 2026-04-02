class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self, root):
        self.root = root

    def print_structure(self, node):
        if node is None:
            return
        print(node.data)
        self.print_structure(node.left)
        self.print_structure(node.right)

b = Node("B")
c = Node("C")
a = Node("A", b, c)

tree = BinaryTree(a)
tree.print_structure(tree.root)