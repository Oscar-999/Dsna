# Iteratively

def linked_list(head):
    values = []
    current = head

    while current is not None:
        values.append(current.val)
        current = current.next
    return values

# Recursively

def linked_list(head):
    values = []
    fill_values(head, values)
    return values

def fill_values(head, values):
    if head is None:
        return
    values.append(head.val)
    fill_values(head.next, values)
