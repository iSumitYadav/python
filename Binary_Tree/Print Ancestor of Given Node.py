class node:
    def __init__(self, key):
        self.data = key
        self.left = self.right = None

def printAncestor(root, target):
    if not root:
        return False

    if root == target:
        return True

    if (printAncestor(root.left, target) | printAncestor(root.right, target)):
        print(root.data, end=" ")
        return True

    return False

root = node(1)
root.left = node(2)
root.right = node(3)
root.left.left = node(4)
root.left.right = node(5)
# setting target to 7
target = root.left.left.left = node(7)

printAncestor(root, target)