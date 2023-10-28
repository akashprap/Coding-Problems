class Solution:
    def beautySum(self, s: str) -> int:
        ans=0
        n=len(s)
        for i in range(n):
            for j in range(i,n):
                cc=Counter(s[i:j+1])
                ans+=max(cc.values())-min(cc.values())
        return ans
        