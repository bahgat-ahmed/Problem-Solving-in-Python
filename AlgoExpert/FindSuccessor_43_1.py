# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


# O(n) time | O(n) space - where n is the number of nodes in the tree
def findSuccessor(tree, node):
    array = inOrderTraverse(tree)
    
    for i in range(len(array)):
        if array[i] == node:
            if i < len(array) - 1:
                return array[i+1]
            return None


def inOrderTraverse(node, array=[]):
    if node is None:
        return
        
    inOrderTraverse(node.left, array)
    array.append(node)
    inOrderTraverse(node.right, array)

    return array
