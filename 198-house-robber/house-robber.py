class Solution:
    # memozation
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
        #tabulation
        # return self.f(0,nums,dp)
        n=len(nums)
        dp=[nums[0]]*(n)
        for ind in range(1,n):
            nottake=dp[ind-1]
            if ind-2>=0:
                take=nums[ind]+dp[ind-2]
            else:
                take=nums[ind]
            dp[ind]=max(nottake,take)
        return dp[n-1]
        