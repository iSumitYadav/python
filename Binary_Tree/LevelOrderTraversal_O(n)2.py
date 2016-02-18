class node:
    def __init__(self, key):
        self.data = key
        self.left = self.right = None

def height(root):
    if root is None:
        return 0

    return max(height(root.left), height(root.right)) + 1

def printSecondary(root, level):
    if root is None:
        return

    if level == 1:
        print(root.data, end = ' ')

    printSecondary(root.left, level-1)
    printSecondary(root.right, level-1)

def printLevelOrder(root):
    h = height(root)

    for x in range(1, h+1):
        printSecondary(root, x)
        print('\n')

root = node(1)
root.left = node(2)
root.right = node(3)
root.left.left = node(4)
root.left.right = node(5)
root.right.left = node(6)
root.right.right = node(7)

print('Level Order of tree is ')
printLevelOrder(root)
print('Level Order Traversal O(n)2')