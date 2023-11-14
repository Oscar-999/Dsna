def sum_list(head):
    total = 0
    current = head

    while current is not None:
        total += current.val
        current = current.next
    return total

# Recursively

def sum_list(head):
    if head is None:
        return 0
    return head.val + sum_list(head.next)
