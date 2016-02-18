class node:
    def __init__(self, key):
        self.data = key
        self.left = self.right = None

def sumprop(root):
    if root is None or (root.left is None and root.right is None):
        return 1

    left_data = 0
    right_data = 0

    if root.left is not None:
        left_data = root.left.data

    if root.right is not None:
        right_data = root.right.data

    if (root.data == left_data + right_data) and sumprop(root.left) and sumprop(root.right):
        return 1
    else:
        return 0

root = node(28)
root.left = node(8)
root.right = node(20)
root.left.left = node(3)
root.left.right = node(5)
root.right.left = node(2)
root.right.right = node(18)

if sumprop(root):
    print("Children Sum Property is Satisfied")
else:
    print("Children Sum Property is NOT Satisfied")