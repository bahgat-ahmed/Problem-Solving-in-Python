# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class TreeInfo:
    def __init__(self, num_visited_nodes, last_node_value):
        self.num_visited_nodes = num_visited_nodes
        self.last_node_value = last_node_value

        
# O(h + k) time | O(h) space - where h is the height of the tree and k is the input parameter
def findKthLargestValueInBst(tree, k):
    tree_info = TreeInfo(0, None)
    reverseInOrderTraverse(tree, k, tree_info)
    return tree_info.last_node_value


def reverseInOrderTraverse(node, k, tree_info):
    if node is None or tree_info.num_visited_nodes >= k:
        return

    
    reverseInOrderTraverse(node.right, k, tree_info)
    if tree_info.num_visited_nodes < k:
        tree_info.num_visited_nodes += 1
        tree_info.last_node_value = node.value
        reverseInOrderTraverse(node.left, k, tree_info)
