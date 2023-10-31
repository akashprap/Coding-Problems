# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def f(prev,ptr):
            if ptr==None:
                return prev
            else:
                temp=ptr.next
                ptr.next=prev
                prev=ptr
                ptr=temp
                return f(prev,ptr)
        return f(None,head)
        # ptr=head
        # prev=None
        # while ptr:
        #     temp=ptr.next
        #     ptr.next=prev
        #     prev=ptr
        #     ptr=temp
        # return prev