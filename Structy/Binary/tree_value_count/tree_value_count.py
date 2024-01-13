
# depth first (recursive)
def tree_value_count(root, target):
  if root is None:
    return 0

  match = 1 if root.val == target else 0

  return match + tree_value_count(root.left, target) + tree_value_count(root.right, target)
# n = number of nodes
# Time: O(n)
# Space: O(n)

# depth first (iterative)
def tree_value_count(root, target):
  if root is None:
    return 0

  count = 0
  stack = [ root ]
  while stack:
    current = stack.pop()
    if current.val == target:
      count += 1

    if current.left is not None:
      stack.append(current.left)
    if current.right is not None:
      stack.append(current.right)

  return count
# n = number of nodes
# Time: O(n)
# Space: O(n)

# breadth first
from collections import deque

def tree_value_count(root, target):
  if root is None:
    return 0

  count = 0
  queue = deque([ root ])
  while queue:
    current = queue.popleft()
    if current.val == target:
      count += 1

    if current.left is not None:
      queue.append(current.left)
    if current.right is not None:
      queue.append(current.right)

  return count
# n = number of nodes
# Time: O(n)
# Space: O(n)
