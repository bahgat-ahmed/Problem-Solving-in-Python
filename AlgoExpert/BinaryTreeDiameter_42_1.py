# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class TreeInfo:
    def __init__(self, diameter, height):
        self.diameter = diameter
        self.height = height

        
# O(n) time | O(h) space (Average Case when the Tree is balanced) or O(n) space (Worst Case when the
# Tree is unbalanced) - where n is the number of nodes in the Binary Tree and h is the height of
# the Binary Tree
def binaryTreeDiameter(tree):
    return getTreeInfo(tree).diameter


def getTreeInfo(sub_tree):
    if sub_tree is None:
        return TreeInfo(0, 0)

    left_tree_info = getTreeInfo(sub_tree.left)
    right_tree_info = getTreeInfo(sub_tree.right)

    longest_path_length = left_tree_info.height + right_tree_info.height
    max_diameter = max(left_tree_info.diameter, right_tree_info.diameter)
    current_diameter = max(max_diameter, longest_path_length)
    current_height = 1 + max(left_tree_info.height, right_tree_info.height)

    return TreeInfo(current_diameter, current_height)
