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
        ptr = head
        for i in range(k):
            if not ptr:
                res.append(None)
                continue
            res.append(ptr)
            size = parts + (1 if extra > 0 else 0)
            extra -= 1
            for j in range(size - 1):
                ptr = ptr.next
            temp = ptr.next
            ptr.next = None
            ptr = temp
        return res
