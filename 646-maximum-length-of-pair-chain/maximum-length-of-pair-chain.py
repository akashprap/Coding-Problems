class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        dp=[1]*len(pairs)
        n=len(pairs)
        pairs.sort()
        for i in range(1,n):
            for j in range(i):
                if pairs[i][0]>pairs[j][1]:
                    if dp[i]<1+dp[j]:
                        dp[i]=1+dp[j]
        return max(dp)