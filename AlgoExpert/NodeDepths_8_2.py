# O(n) time | O(h) space - where n is the number of nodes in the Binary Tree
# and h is the height of the Binary Tree
def nodeDepths(root):
	depthsSum = 0
	stack = [{"node": root, "depth": 0}]
	while len(stack) > 0:
		# pop the last dictionary in the stack
		currentNode = stack.pop()
		node, depth = currentNode["node"], currentNode["depth"]
		
		if node is None:
			# the node is a leaf node
			continue
		depthsSum += depth
		# push the current node's children into the stack
		stack.append({"node": node.left, "depth": depth + 1})
		stack.append({"node": node.right, "depth": depth + 1})
	return depthsSum
		

# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
