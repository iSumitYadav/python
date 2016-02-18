class node:
    def __init__(self, key):
        self.data = key
        self.left = self.right = None

def kdistroot(root, k, level):
    if not root: # is None:
        return

    if level == k:
        print(root.data, end = ' ')

    level += 1
    kdistroot(root.left, k, level)
    kdistroot(root.right, k, level)

root = node(1)
root.left = node(2)
root.right = node(3)
root.left.left = node(4)
root.left.right = node(5)
root.right.left = node(6)
root.right.right = node(7)
root.right.right.left = node(8)
root.right.right.right = node(9)

k = int(input("Enter k :"))     #Never Forget to typecast input in Python :)
level = 0   #Preseted to zero
# k=2
kdistroot(root, k, level)