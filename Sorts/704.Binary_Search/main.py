from collections import deque
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if root is None:
            return []

        stack = [root]
        res = []

        while stack:
            current = stack.pop()

            if current:
                stack.append(current.right)  # Push right child
                stack.append(current.val)    # Push current node value
                stack.append(current.left)   # Push left child

            # Process nodes in the order: left, current, right

        return res
