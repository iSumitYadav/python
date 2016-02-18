class node:
    def __init__(self, key):
        self.data = key
        self.left = self.right = None

def maxWidth(root):
    if root is None:
        return

    queue = []
    maxwidth = width = 0
    queue.append(root)
    queue.append(None)
    #print("len of queue", len(queue))

    while(len(queue) > 0):
        #print(width)
        temp = queue.pop(0)

        if temp is None:
            if maxwidth < width:
                maxwidth = width
                width = 0
                print(maxwidth, end = ' ')

            if len(queue) == 0:
                return maxwidth

            queue.append(None)

        else:

            if temp.left is not None:
                queue.append(temp.left)
                width += 1

            if temp.right is not None:
                queue.append(temp.right)
                width += 1

root = node(1)
root.left = node(2)
root.right = node(3)
root.left.left = node(4)
root.left.right = node(5)
#root.right.left = node(6)
root.right.right = node(7)
root.right.right.left = node(8)
root.right.right.right = node(9)

def inorder(root):
    if root is None:
        return

    inorder(root.left)
    print(root.data, end = ' ')
    inorder(root.right)

print("\nMax Width : ", maxWidth(root))
#inorder(root)