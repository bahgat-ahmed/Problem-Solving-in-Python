# O(n) time | O(h) space - where n is the number of nodes in the Binary Tree
# and h is the height of the Binary Tree
def nodeDepths(root):
	depths = []
	calculateNodeDepths(root, 0, depths)
	return sum(depths)

# O(n) time | O(n) space - where n is the number of nodes in the Binary Tree
def calculateNodeDepths(node, depth, depths):
	if node is None:
		return

	depths.append(depth)
		
	calculateNodeDepths(node.left, depth + 1, depths)
	calculateNodeDepths(node.right, depth + 1, depths)
	
	
# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
