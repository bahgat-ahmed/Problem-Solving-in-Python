# O(n) time | O(d) space - where n is the number of nodes in the Binary Tree and d is the depth (height)
# of the Binary Tree (hence: d is log(n) in binary trees)
# recursive solution
def invertBinaryTree(tree):
    if tree is None:
        return
    swapRightAndLeft(tree)
    invertBinaryTree(tree.right)
    invertBinaryTree(tree.left)


def swapRightAndLeft(subtree):
    subtree.right, subtree.left = subtree.left, subtree.right

    
# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
