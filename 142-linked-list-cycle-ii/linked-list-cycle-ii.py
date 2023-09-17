# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        i=0
        d=defaultdict()
        while head:
            if head in d:
                return head
            d[head]=i
            i+=1
            head=head.next
        return None