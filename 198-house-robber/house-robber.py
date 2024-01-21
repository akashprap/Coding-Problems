class Solution:
    def f(self,ind,nums,dp):
        if ind>=len(nums):
            return 0
        if (ind) in dp:
            return dp[ind]
        nottake=self.f(ind+1,nums,dp)
        take=nums[ind]+self.f(ind+2,nums,dp)
        dp[ind]= max(take,nottake)
        return dp[ind]
    def rob(self, nums: List[int]) -> int:
        dp={}
        return self.f(0,nums,dp)
        