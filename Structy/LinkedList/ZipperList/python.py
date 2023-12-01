def zipper_lists(head_1,head_2):
    tail=head_1
    current_1 = head_1.next
    current_2 = head_2
    count = 0

    while current_1 is not None and current_2 is not None:
        if count % 2 == 0:
            tail = current_2
            current_2 = current_2.next
        else:
            tail = current_1
            current_1 = current_1.next
        tail = tail.next
        count += 1

    if current_1 is not None:
        tail.next = current_1
    if current_2 is not None:
        tail.next = current_2

    return head_1


# Recursion

def zipper_lists(head_1,head_2):
    if head_1 is None and head_2 is None:
        return None
    if head_1 is None:
        return head_2
    if head_2 is None:
        return head_1
    next_1 = head_1.next
    next_2 = head_2.next
    head_1.next = head_2
    head_2.next = zipper_lists(next_1,next_2)

    return head_1
