def how_high(node):
    if node is None:
        return -1
    left_height = how_high(node.left)
    right_height = how_high(node.right)

    return 1+ max(left_height,right_height)
# n = number of nodes
# Time: 0(n)
# Space: 0(n)

