def remove_node(head, target_val):
    if head.val == target_val:
        return head.next
    curr = head
    prev = None

    while curr:
        if curr.val == target_val:
            prev.next = curr.next
            break
        prev = curr
        curr = curr.next
    return head
# Iterative
# time : 0(n)
# space: 0(1)

def remove_node(head, target_val):
    if head is None:
        return None

    if head.val == target_val:
        return head.next

    head.next = remove_node(head.next, target_val)

    return head

#recursive
#Time: 0(n)
#space: 0(n)
