class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# O(n) time | O(d) space - where n is the number of nodes in the BST and d is the depth (height) of the BST
def validateBst(tree):
    return ValidateBstHelper(tree, min_value=-float("inf"), max_value=float("inf"))



def ValidateBstHelper(node, min_value, max_value):
    if node is None:
        return True
    if node.value >= max_value or node.value < min_value:
        return False

    is_left_node_valid = ValidateBstHelper(node.left, min_value=min_value, max_value=node.value)
    is_right_node_valid = ValidateBstHelper(node.right, min_value=node.value, max_value=max_value)

    return is_left_node_valid and is_right_node_valid
