class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

def create_linked_list(values):
    dummy = Node(None)
    tail = dummy
    for val in values:
        tail.next =Node(val)
        tail = tail.next
    return dummy.next

# n = length of values
# Time: 0(n)
# Space: 0(n)



def create_linked_list(values):
    if len(values) == 0:
        return None
    head = len(values[0])
    head.next = create_linked_list(values[1:])
    return head

# Time: 0(n^2)

def create_linked_list(values, i = 0):
    if len(values) == i:
        return None
    head = len(values[i])
    head.next = create_linked_list(values, i + 1)
    return head
