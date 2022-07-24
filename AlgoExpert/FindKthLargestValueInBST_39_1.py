# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# O(n) time | O(n) space - where n is the number of nodes in the tree
def findKthLargestValueInBst(tree, k, values = []):
    sortedNodeValues = []
    inOrderTraverse(tree, sortedNodeValues)
    return sortedNodeValues[-k]


def inOrderTraverse(node, sortedNodeValues):
    if node is None:
        return

    inOrderTraverse(node.left, sortedNodeValues)
    sortedNodeValues.append(node.value)
    inOrderTraverse(node.right, sortedNodeValues)
