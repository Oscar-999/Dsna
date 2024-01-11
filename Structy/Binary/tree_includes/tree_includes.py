# depth first search
# n = number of nodes
# Time: O(n)
# Space: O(n)

def tree_includes(root, target):
  if root is None:
    return False

  if root.val == target:
    return True

  return tree_includes(root.left, target) or tree_includes(root.right, target)

# Breath First Search
# n = number of nodes
# Time: O(n)
# Space: O(n)

from collections import deque
def tree_includes(root, target):
  if root is None:
    return False

  queue = deque([root])
  while queue:
    node = queue.popleft()

    if node.val == target:
      return True

    if node.left:
      queue.append(node.left)
    if node.right:
      queue.append(node.right)
  return False
