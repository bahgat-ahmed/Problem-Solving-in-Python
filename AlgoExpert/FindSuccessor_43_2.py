# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


# O(h) time | O(1) space - where h is the height of the tree
def findSuccessor(tree, node):
    if node.right is not None:
        return getLeftMostChild(node.right)

    return getRightMostParent(node)


def getLeftMostChild(node):
    current_node = node
    while current_node.left is not None:
        current_node = current_node.left
        
    return current_node


def getRightMostParent(node):
    current_node = node
    while current_node.parent is not None and current_node.parent.right == current_node:
        current_node = current_node.parent
        
    return current_node.parent
