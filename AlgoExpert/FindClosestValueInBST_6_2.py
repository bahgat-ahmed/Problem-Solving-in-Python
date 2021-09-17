# Average: O(log(n)) time | O(1) space
# Worst: O(n) time | O(1) space
# - where n is the number of nodes in the BST
def findClosestValueInBst(tree, target):
	
	current_node = tree
	closest = float('inf')
	
	while current_node is not None:
		if abs(target - closest) > abs(target - current_node.value):
			closest = current_node.value
			
		if target < current_node.value:
			current_node = current_node.left
		elif target > current_node.value:
			current_node = current_node.right
		else:
			# we found the exact value
			break
		
	return closest


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
