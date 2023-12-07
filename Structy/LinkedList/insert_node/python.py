class Node:
    def __init__(self,val):
        self.val = val
        self.next = None


    def insert_node(head, value, index):
        if index == 0:
            new_node = Node(value)
            new_node.next = head
            return new_node
        counter = 0
        curr = head
        while curr:
            if index - 1 == counter:
                next = curr.next
                curr.next = Node(value)
                curr.next.next = next
            counter +=1
            curr = curr.next
        return head
#n = number of nodes
#Time: 0(n)
#Space: O(1)



def insert_node(head,value,index,count = 0):
    if index == 0:
        new_head = Node(value)
        new_head.next = head
        return new_head

    if head is None:
        return None

    if count == index -1:
        temp = head.next
        head.next = Node(value)
        head.next.next = temp
        return
    
    insert_node(head.next,value,index, count + 1)
    return head
