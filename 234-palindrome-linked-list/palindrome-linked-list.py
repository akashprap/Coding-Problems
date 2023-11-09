# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self,ptr):
        prev=None
        while ptr:
            nextt=ptr.next
            ptr.next=prev
            prev=ptr
            ptr=nextt
        return prev

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow=head
        fast=head
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
        mid=slow.next
        midptr=self.reverse(mid)
        while head and midptr:
            if head.val==midptr.val:
                head=head.next
                midptr=midptr.next
            else:
                return False
        return True
        