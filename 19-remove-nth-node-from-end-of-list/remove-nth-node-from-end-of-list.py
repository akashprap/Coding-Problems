# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length=0
        ptr=head
        while ptr:
            length+=1
            ptr=ptr.next
        rem=length-n
        # print(rem)
        if rem==0:
            if head.next:
                return head.next
            return None
        cur=head
        while rem-1:
            rem-=1
            cur=cur.next
            
        if cur.next:
            # print(cur.val)
            if cur.next.next:
                cur.next=cur.next.next
            else:
                cur.next=None
        else:
            cur.next=None
        return head