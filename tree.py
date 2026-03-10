# Tree

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

root = Node(10)
root.left = Node(20)
root.right = Node(30)

print("Root:", root.data)
print("Left Child:", root.left.data)
print("Right Child:", root.right.data)