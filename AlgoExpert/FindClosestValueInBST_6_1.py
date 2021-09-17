# Average: O(log(n)) time | O(log(n)) space
# Worst: O(n) time | O(n) space
# - where n is the number of nodes in the BST
def findClosestValueInBst(tree, target):
    return findClosestValueHelper(tree, target, float('inf'))

def findClosestValueHelper(tree, target, closest):
	# this is the base case which must exist for any recursive
	# solution to terminate on it
	if tree is None:
		return closest
	
	if abs(target - closest) > abs(target - tree.value):
		closest = tree.value
						   
	if target < tree.value:
		return findClosestValueHelper(tree.left, target, closest)
	elif target > tree.value:
		return findClosestValueHelper(tree.right, target, closest)
	else:
		return closest

# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
