# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# O(n) time | O(n) space - where n is the number of nodes in the Binary Tree
def branchSums(root):
	sums = []
	calculateBranchSums(root, 0, sums)
	return sums
	
def calculateBranchSums(currentNode, running_sum, sums):
	if currentNode is None:
		return
	
	running_sum += currentNode.value
	if currentNode.left is None and currentNode.right is None:
		sums.append(running_sum)
		return
	
	calculateBranchSums(currentNode.left, running_sum, sums)
	calculateBranchSums(currentNode.right, running_sum, sums)

