# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# O(h + k) time | O(h) space - where h is the height of the tree and k is the input parameter
def findKthLargestValueInBst(tree, k):
    count = 0
    stack = []
    current_node = tree

    while stack or current_node:
        if current_node:
            stack.append(current_node)
            current_node = current_node.right
        else:
            current_node = stack.pop()
            count += 1
            if count == k:
                return current_node.value
            current_node = current_node.left
                
