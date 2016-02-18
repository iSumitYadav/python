class node:
    def __init__(self, key):
        self.data = key
        self.left = self.right = None

def inorder(root):

    if root is None:
        return

    stack = []

    while(1):

        if root is not None:
            stack.append(root)
            root = root.left
        else:
            if not stack:
                break

            root = stack.pop()
            print(root.data, end = ' ')
            root = root.right

root = node(1)
root.left = node(2)
root.right = node(3)
root.left.left = node(4)
root.left.right = node(5)
root.right.left = node(6)
root.right.right = node(7)

print('InOrder tarversal Using Stack:', end = ' ')
inorder(root)