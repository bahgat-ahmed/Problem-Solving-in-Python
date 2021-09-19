# Similar to Solution 1 but simpler (i.e. it is also recursive)

# O(n) time | O(h) space - where n is the number of nodes in the Binary Tree
# and h is the height of the Binary Tree
def nodeDepths(root, depth = 0):
    if root is None:
		# because we are adding so 0 will add nothing
		return 0
	return depth + nodeDepths(root.left, depth + 1) + nodeDepths(root.right, depth + 1)


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
