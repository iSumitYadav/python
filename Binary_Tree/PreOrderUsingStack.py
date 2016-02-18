class node:
    def __init__(self, key):
        self.data = key
        self.left = self.right = None

def preorder(root):
    if root is None:
        return

    stack = []

    while(1):
        if root is not None:
            print(root.data, end = ' ')
            stack.append(root)
            root = root.left
        else:
            if not stack: # Can't use "if stack is None" bc :(
                break

            root = stack.pop()
            root = root.right

root = node(1)
root.left = node(2)
root.right = node(3)
root.left.left = node(4)
root.left.right = node(5)
root.right.left = node(6)
root.right.right = node(7)

print('PreOrder tarversal Using Stack:', end = ' ')
preorder(root)