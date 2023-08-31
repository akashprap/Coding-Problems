class Solution:
    def jump(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[1e9]*n
        dp[0]=0
        for i in range(n):
            for j in range(i+1,min(nums[i]+i+1,n)):
                dp[j]=min(dp[j],1+dp[i])
        return dp[n-1] if dp[n-1]!=1e9 else -1