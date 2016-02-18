class node:
    def __init__(self, key):
        self.data = key
        self.left = self.right = None

def are_identical(root1, root2):
    if not root1 and not root2:
        return 1

    if not root1 or not root2:
        return 0

    return (root1.data == root2.data) \
           and are_identical(root1.left, root2.left) \
           and are_identical(root1.right, root2.right)

root1 = node(1)
root1.left = node(2)
root1.right = node(3)
root1.left.left = node(4)
root1.left.right = node(5)

root2 = node(1)
root2.left = node(2)
root2.right = node(3)
root2.left.left = node(4)
root2.left.right = node(6) # Changed node

# if(are_identical(root1, root2)):
#     print("True")
# else:
#     print("False")

print("True") if are_identical(root1, root2) else print("False")