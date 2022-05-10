# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # Average: O(log(n)) time | O(1) space
		# Worst: O(n) time | O(1) space
		bst_pointer = self
		while True:
			if value < bst_pointer.value:
				if bst_pointer.left is None:
					bst_pointer.left = BST(value)
					break
				else:
					bst_pointer = bst_pointer.left
			else:
				if bst_pointer.right is None:
					bst_pointer.right = BST(value)
					break
				else:
					bst_pointer = bst_pointer.right
				
		return self	
    
	# Average: O(log(n)) time | O(1) space
	# Worst: O(n) time | O(1) space
    def contains(self, value):
        bst_pointer = self
		while bst_pointer is not None:
			if value > bst_pointer.value:
				bst_pointer = bst_pointer.right					
			elif value < bst_pointer.value:
				bst_pointer = bst_pointer.left
			else:
				return True
		return False

	# Average: O(log(n)) time | O(1) space
	# Worst: O(n) time | O(1) space
    def remove(self, value, parent_pointer=None):
		bst_pointer = self
		while bst_pointer is not None:
			if value > bst_pointer.value:
				parent_pointer = bst_pointer
				bst_pointer = bst_pointer.right
			elif value < bst_pointer.value:
				parent_pointer = bst_pointer
				bst_pointer = bst_pointer.left
			else:
				# found the value to be removed
				if bst_pointer.left is not None and bst_pointer.right is not None:
					bst_pointer.value = bst_pointer.right.get_min_value()
					bst_pointer.right.remove(bst_pointer.value, bst_pointer)
				elif parent_pointer is not None:
					if parent_pointer.left == bst_pointer:
						parent_pointer.left = bst_pointer.left if bst_pointer.left is not None else bst_pointer.right
					elif parent_pointer.right == bst_pointer:
						parent_pointer.right = bst_pointer.left if bst_pointer.left is not None else bst_pointer.right
				# if it is the root node
				elif parent_pointer is None:
					if bst_pointer.right is not None:
						bst_pointer.value = bst_pointer.right.value
						# the order of the next two operations is critical
						bst_pointer.left = bst_pointer.right.left
						bst_pointer.right = bst_pointer.right.right
					elif bst_pointer.left is not None:
						bst_pointer.value = bst_pointer.left.value
						# the order of the next two operations is critical
						bst_pointer.right = bst_pointer.left.right
						bst_pointer.left = bst_pointer.left.left
					else:
						# this is a single-node tree; do nothing
						pass
				break
				
		return self

	# Average: O(log(n)) time | O(1) space
	# Worst: O(n) time | O(1) space
    def get_min_value(self):
		bst_pointer = self
		while bst_pointer.left is not None:
			bst_pointer = bst_pointer.left
		return bst_pointer.value
		