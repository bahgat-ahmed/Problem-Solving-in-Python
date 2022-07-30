# O(n) time | O(n) space
# iterative solution
def invertBinaryTree(tree):
    queue = [tree]
    while len(queue):
        current = queue.pop(0)
        if current is None:
            continue
        swapRightAndLeft(current)
        queue.append(current.left)
        queue.append(current.right)
        

def swapRightAndLeft(subtree):
    subtree.right, subtree.left = subtree.left, subtree.right

    
# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
