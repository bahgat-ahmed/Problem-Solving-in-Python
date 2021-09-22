# Do not edit the class below except
# for the depthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self
	# Iterative solution
	# O(v + e) time | O(v) space - where v is the number of vertices and e
	# is the number of edges of the input graph
    def depthFirstSearch(self, array):
        if self.name is None:
			return array

		stack = [{"name": self.name, "children": self.children}]
		while len(stack) > 0:
			graphNode = stack.pop()
			name, children = graphNode["name"], graphNode["children"]
			array.append(name)
			if children == []:
				continue
	
			for child in reversed(children):
				stack.append({"name": child.name, "children": child.children})

		return array