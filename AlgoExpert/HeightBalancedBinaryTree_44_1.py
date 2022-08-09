# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class TreeInfo:
    def __init__(self, is_balanced, height):
        self.is_balanced = is_balanced
        self.height = height


def heightBalancedBinaryTree(tree):
    return is_subtree_balanced_fn(tree).is_balanced


# O(n) time | O(h) space - where n is the number of nodes in the binary tree, and h is the height of
# the binary tree
def is_subtree_balanced_fn(subtree):
    if subtree is None:
        return TreeInfo(True, -1)

    left_subtree_info = is_subtree_balanced_fn(subtree.left)
    right_subtree_info = is_subtree_balanced_fn(subtree.right)

    is_subtree_balanced = (
        left_subtree_info.is_balanced
        and right_subtree_info.is_balanced
        and abs(left_subtree_info.height - right_subtree_info.height) <= 1
    )
    subtree_height = max(left_subtree_info.height, right_subtree_info.height) + 1
    return TreeInfo(is_subtree_balanced, subtree_height)
