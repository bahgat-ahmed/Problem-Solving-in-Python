# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class TreeInfo:
    def __init__(self, root_idx):
        self.root_idx = root_idx


# O(n) time | O(n) space - where n is the length of the input array
def reconstructBst(preOrderTraversalValues):
    tree_info = TreeInfo(0)
    return reconstructBstFromRange(float('-inf'), float('inf'), preOrderTraversalValues, tree_info)


def reconstructBstFromRange(lower_bound, upper_bound, preOrderTraversalValues, current_sub_tree_info):
    if current_sub_tree_info.root_idx == len(preOrderTraversalValues):
        return None

    root_value = preOrderTraversalValues[current_sub_tree_info.root_idx]
    if root_value < lower_bound or root_value >= upper_bound:
        return None

    current_sub_tree_info.root_idx += 1
    left_sub_tree = reconstructBstFromRange(lower_bound, root_value, preOrderTraversalValues, current_sub_tree_info)
    right_sub_tree = reconstructBstFromRange(root_value, upper_bound, preOrderTraversalValues, current_sub_tree_info)
    return BST(root_value, left_sub_tree, right_sub_tree)
