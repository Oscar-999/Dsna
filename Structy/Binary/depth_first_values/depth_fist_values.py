class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
# n = number of nodes
# Time: O(n)
# Space: O(n)
def depth_first_values(root):
    if not root:
        return []

    stack = [root]
    values = []

    while stack:
        node = stack.pop()
        values.append(node.val)

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return values
