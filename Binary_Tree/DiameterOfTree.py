class node:
    def __init__(self, key):
        self.data = key
        self.left = self.right = None

class ht:
    def __init__(self):
        h = 0

def dia(root, height):

    if root is None:
        height.h = 0
        return 0    # Diameter is also zero

    #print(root.data, end = ' ')
    lh = ht()
    rh = ht()
    lh.h += 1
    rh.h += 1
    ldia = dia(root.left, lh)
    rdia = dia(root.right, rh)

    height.h = max(lh.h, rh.h) + 1

    return max(lh.h + rh.h + 1, max(ldia, rdia))

def diameter(root):
    height = ht()
    dia(root, height)

root = node(1)
root.left = node(2)
root.right = node(3)
root.left.left = node(4)
root.left.right = node(5)
root.right.left = node(6)
root.right.right = node(7)

print('Diameter of Tree:', end = ' ')
d = diameter(root)
print(d)
