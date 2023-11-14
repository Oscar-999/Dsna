def find_target(head, target):
    current = head
    while current is not None:
        if current.val == target:
            return True
        current = current.next
    return False


def find_target(head, target):
    if head is None:
        return False
    if head == target:
        return True
    return find_target(head.next, target)
