class node:
    def __init__(self, key):
        self.data = key
        self.left = self.right = None

def func(root, sum, k):
    if root is None:
        return 0

    sum = sum + root.data

    if sum > k:
        return 0
    elif sum == k and not root.left and not root.right:
        return 1
    else:
        return func(root.left, sum, k) or func(root.right, sum, k)

def isPath(root, k):
    if not root:
        return 0

    return func(root, 0, k)

root = node(10)
root.left = node(8)
root.right = node(2)
root.left.left = node(3)
root.left.right = node(5)
root.right.left = node(2)

k = 14

if isPath(root, k):
    print("Path Exist!\n")
else:
    print("Path DOESN'T Exist!\n")