# Iteraterative o(n) o(1)

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

# recursive o(n) o(n)

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pass
