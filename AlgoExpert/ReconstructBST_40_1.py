# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# O(n^2) time | O(n) space - where n is the length of the input array
def reconstructBst(preOrderTraversalValues):
    if len(preOrderTraversalValues) == 0:
        return None

    current_value = preOrderTraversalValues[0]
    right_subtree_root_idx = len(preOrderTraversalValues)

    for idx in range(1, len(preOrderTraversalValues)):
        value = preOrderTraversalValues[idx] 
        if value >= current_value:
            right_subtree_root_idx = idx
            break
    

    left_sub_tree = reconstructBst(preOrderTraversalValues[1:right_subtree_root_idx])
    right_sub_tree = reconstructBst(preOrderTraversalValues[right_subtree_root_idx:])
    return BST(current_value, left_sub_tree, right_sub_tree)
            
