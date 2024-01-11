class Node:
    def __init__(self,val):
        self.val = val
        self.right = None
        self.left = None

def breath_first_values(root):
    if not root:
        return []

    queue = [ root ]
    values = []

    while queue:
        node = queue.pop(0)
        values.append(node.val)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return values

# Time: 0(n^2)
# line 15 the pop on an array will make it 0(n)


from collections import deque
def breath_first_values(root):
    if not root:
        return []

    queue = deque[ root ]
    values = []

    while queue:
        node = queue.popleft()
        values.append(node.val)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return values
# n = number of nodes
# Time: O(n)
# Space: O(n)
