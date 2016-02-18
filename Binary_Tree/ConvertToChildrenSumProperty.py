class node:
    def __init__(self, key):
        self.data = key
        self.left = self.right = None

def convertTree(root):
    if root is None or (root.left == None and root.right == None):
        return

    convertTree(root.left)
    convertTree(root.right)

    left_data = right_data = 0

    if root.left is not None:
        left_data = root.left.data

    if root.right is not None:
        right_data = root.right.data

    diff = left_data + right_data - root.data

    if diff > 0:
        root.data = root.data + diff
    elif diff < 0:
        increment(root, -diff)

def increment(node, diff):
    if node.left is not None:
        node.left.data = node.left.data + diff
        increment(node.left, diff)

    elif node.right is not None:
        node.right.data = node.right.data + diff
        increment(node.right, diff)

def inorder(root):
    if root is None:
        return

    inorder(root.left)
    print(root.data, end = " ")
    inorder(root.right)

root = node(50)
root.left = node(7)
root.right = node(2)
root.left.left = node(3)
root.left.right = node(5)
root.right.left = node(1)
root.right.right = node(30)

print("Inorder Traversal BEFORE ChldrenSumProperty")
inorder(root)

convertTree(root)

print("\n\nInorder Traversal AFTER ChldrenSumProperty")
inorder(root)