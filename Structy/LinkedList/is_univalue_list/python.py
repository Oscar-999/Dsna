def is_univalue_list(head):
    current = head

    while current:
        if head.val != current:
            return False
        current = current.next

    return True

# n = number of nodes
# Time: O(n)
# Space: O(1)



# n = number of nodes
# Time: O(n)
# Space: O(n)


def is_univalue_list(head, prev_value=None):
    if head is None:
        return True

    if prev_value is None or head.val == prev_value:
        return is_univalue_list(head.next, head.val)
    else:
        return False
