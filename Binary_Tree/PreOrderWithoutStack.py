class node:
    def __init__(self, key):
        self.data = key
        self.left = self.right = None

def preorder(root):
    if root is None:
        return

    while(root):
        if not root.left:# is None:
            print(root.data, end = ' ')
            root = root.right
        else:
            temp = root.left
            while(temp.right and temp.right is not root): # 2nd condition is IMP
                temp = temp.right

            if temp.right == root:
                root = root.right
                temp.right = None
            else:
                print(root.data, end = ' ')
                temp.right = root
                root = root.left

root = node(1)
root.left = node(2)
root.right = node(3)
root.left.left = node(4)
root.left.right = node(5)
root.right.left = node(6)
root.right.right = node(7)

print('PreOrder tarversal Using Stack:', end = ' ')
preorder(root)