class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def max_math_sum(root):
    if root is None:
        return float("-inf")

    if root.left is None and root.right is None:
        return root.val

    max_left = max_math_sum(root.left)
    max_right = max_math_sum(root.right)

    return root.val + max(max_left, max_right)

# depth first recursive
# n = number of nodes
# Time: O(n)
# Space: O(n)
