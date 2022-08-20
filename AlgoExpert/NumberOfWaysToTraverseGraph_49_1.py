# O(2^(n + m)) time | O(n + m) space - where n is the width of the graph
# and m is its height
def numberOfWaysToTraverseGraph(width, height):
    if width == 1 or height == 1:
        return 1

    return numberOfWaysToTraverseGraph(width - 1, height) + numberOfWaysToTraverseGraph(width, height - 1)
