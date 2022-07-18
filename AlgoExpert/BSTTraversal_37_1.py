# O(n) time | O(n) space - where n is the number of nodes in the Binary Search Tree "BST"
def inOrderTraverse(tree, array):
    if tree is not None:
        inOrderTraverse(tree.left, array)
        array.append(tree.value)
        inOrderTraverse(tree.right, array)
    return array    


# O(n) time | O(n) space - where n is the number of nodes in the Binary Search Tree "BST"
def preOrderTraverse(tree, array):
    if tree is not None:
        array.append(tree.value)
        preOrderTraverse(tree.left, array)
        preOrderTraverse(tree.right, array)
    return array    


# O(n) time | O(n) space - where n is the number of nodes in the Binary Search Tree "BST"
def postOrderTraverse(tree, array):
    if tree is not None:
        postOrderTraverse(tree.left, array)
        postOrderTraverse(tree.right, array)
        array.append(tree.value)
    return array    
