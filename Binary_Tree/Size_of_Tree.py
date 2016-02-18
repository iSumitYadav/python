class node:
    def __init__(self, key):
        self.data = key
        self.left = self.right = None

def size(root):
    if not root:
        return 0

    tree_size = size(root.left) + size(root.right) + 1

    return tree_size

root = node(1)
root.left = node(2)
root.right = node(3)
root.left.left = node(4)
root.left.right = node(5)
root.right.left = node(6)
root.right.right = node(7)
# root.right.right.right = node(8)

print(size(root))