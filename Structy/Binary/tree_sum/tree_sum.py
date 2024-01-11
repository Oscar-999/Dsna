# DepthFirstTraversal

def tree_sum(root):
    if root is None:
        return 0
    return root.val + tree_sum(root.left) + tree_sum(root.right)

from collections import deque
# Breath first

def tree_sum(root):
    if root is None:
        return 0

    queue = deque([root])
    sum = 0
