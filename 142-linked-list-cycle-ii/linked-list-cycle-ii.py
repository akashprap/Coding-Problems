class Solution:
    def detectCycle(self,head):
        dp={}
        while head:
            if head in dp: return head
            dp[head]=1
            head=head.next