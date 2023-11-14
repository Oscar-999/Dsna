def get_node_value(head, index):
    count = 0
    current = head
    while current is not None:
        if count == index:
            return current.val
        count += 1
        current = current.next


def get_node_value(head, index):
    if head is None:
        return None
    if index == 0:
        return head.val
    return get_node_value(head.next, index - 1)
