# DepthFirstTraversal

def tree_sum(root):
    if root is None:
        return 0
    return root.val + tree_sum(root.left) + tree_sum(root.right)
# n = number of nodes
# Time: O(n)
# Space: O(n)

# breadth first
from collections import deque

def tree_sum(root):
  if not root:
    return 0

  queue = deque([ root ])
  total_sum = 0
  while queue:
    node = queue.popleft()

    total_sum += node.val

    if node.left:
      queue.append(node.left)

    if node.right:
      queue.append(node.right)

  return total_sum
# n = number of nodes
# Time: O(n)
# Space: O(n)
