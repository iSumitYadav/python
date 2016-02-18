class node:
    def __init__(self, key):
        self.data = key
        self.left = self.right = None

def areIdentical(t, s):
    if t == None and s == None:
        return True

    if t == None or s == None:
        return False

    return (t.data == s.data and areIdentical(t.left, s.left) and areIdentical(t.right, s.right))

def subtree(t, s):
    if s is None:
        return True

    if t is None:
        return False

    if areIdentical(t, s):
        return True

    return subtree(t.left, s) or subtree(t.right, s)

t = node(26)
t.left = node(10)
t.right = node(3)
t.left.left = node(4)
t.left.right = node(6)
t.right.right = node(3)
t.left.left.right = node(30)

s = node(10)
s.left = node(4)
s.right = node(6)
s.left.right = node(30)

if subtree(t, s):
    print("S is Subtree of T")
else:
    print("S is Not a Subtree of T")