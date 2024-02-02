# solutions
# depth first (recursive)
def tree_min_value(root):
  if root is None:
    return float("inf")
  smallest_left_value = tree_min_value(root.left)
  smallest_right_value = tree_min_value(root.right)
  return min(root.val, smallest_left_value, smallest_right_value)
# n = number of nodes
# Time: O(n)
# Space: O(n)

# depth first (iterative)
def tree_min_value(root):
  stack = [ root ]
  smallest = float("inf")
  while stack:
    current = stack.pop()
    if current.val < smallest:
      smallest = current.val

    if current.left is not None:
      stack.append(current.left)
    if current.right is not None:
      stack.append(current.right)

  return smallest
# n = number of nodes
# Time: O(n)
# Space: O(n)


# breadth first (iterative)
from collections import deque

def tree_min_value(root):
  queue = deque([ root ])
  smallest = float("inf")
  while queue:
    current = queue.popleft()
    if current.val < smallest:
      smallest = current.val

    if current.left is not None:
      queue.append(current.left)
    if current.right is not None:
      queue.append(current.right)

  return smallest
# n = number of nodes
# Time: O(n)
# Space: O(n)


def tree_min_value(root):
  min_val = float("inf")
  queue = deque([root])

  while queue:
    node = queue.popleft()
    if min_val > node.val:
      min_val = node.val

    if node.left:
      queue.append(node.left)
    if node.right:
      queue.append(node.right)
  return min_val



