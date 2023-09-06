class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        n = 0
        ptr = head
        while ptr:
            n += 1
            ptr = ptr.next
        parts = n // k
        extra = n % k
        res = []
        cur = head
        for i in range(k):
            size = parts + (1 if i < extra else 0)
            dummy = ListNode(None)
            current = dummy
            for j in range(size):
                current.next = ListNode(cur.val)
                current = current.next
                if cur:
                    cur = cur.next
            res.append(dummy.next)
        return res
