def merge_list(head_1,head_2):
    dummy = node = Node(None)
    current_1 = head_1
    current_2 = head_2

    while current_1 and current_2:
        if current_1.val < current_2.val:
            tail = current_1
            current_1 = current_1.next
        else:
            tail = current_2
            current_2 = current_2.next
        tail = tail.next

    tail.next = current_1 or current_2

    return dummy.next

# n = length of list 1
# m = length of list 2
# time complextity = 0(min(n,m))
# space = 0(1)


# Recursion
# space = 0(n)

def merge_list(head_1, head_2):
    if head_1 is None and head_2 is None:
        return None
    if head_1 is None:
        return head_2
    if head_2 is None:
        return head_1

    if head_1.val < head_2.val:
        next_1 = head_1.next
        head_1.next = merge_list(next_1, head_2)
        return head_1
    else:
        next_2 = head_2.next
        head_2.next = merge_list(head_1, next_2)
        return head_2
