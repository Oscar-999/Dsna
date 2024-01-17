def leaf_list(root):
    if root is None:
        return []
    stack = [root]
    leaves = []

    while stack:
        node = stack.pop()

        if node.left is None and node.right is None:
            leaves.append(node.val)

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return leaves

def leaf_list(root):
    leaves = []
    _leaf_list(root,leaves)
    return leaves

def _leaf_list(root, leaves):
    if root is None:
        return
    if root.left is None and root.right is None:
        leaves.append(root.val)

    _leaf_list(root.left, leaves)
    _leaf_list(root.right, leaves)
