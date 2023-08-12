#User function Template for python3
import bisect
class Solution:
    # def f(self,ind,arr,prev,dp):
    #     if ind==-1:
    #         return 0
    #     if (ind,prev) in dp:
    #         return dp[(ind,prev)]
    #     take=0
    #     nottake=0
    #     if arr[ind]<arr[prev] or prev==-1:
    #         take=1+self.f(ind-1,arr,ind,dp)
    #     nottake=self.f(ind-1,arr,prev,dp)
    #     dp[(ind,prev)]= max(take,nottake)
    #     return dp[(ind,prev)]
    
    #Function to find length of longest increasing subsequence.
    def longestSubsequence(self,nums,n):
        # code here
        # dp={}
        # return self.f(n-1,a,-1,dp)
        
        
        # maxi=1
        # dp=[1]*n
        # for ind in range(1,n):
        #     for prev in range(ind):
        #         if a[ind]>a[prev]:
        #             dp[ind]=max(dp[ind],1+dp[prev])
        #             # maxi=max(maxi,dp[ind])
        # return max(dp)
        
        
        if n==0:
            return 0
        ans=[]
        ans.append(nums[0])
        for i in range(1,n):
            if nums[i]>ans[-1]:
                ans.append(nums[i])
            else:
                ind=bisect.bisect_left(ans,nums[i])
                ans[ind]=nums[i]
        return len(ans)
       



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        a = [ int(x) for x in input().split() ]
        ob=Solution()
        print(ob.longestSubsequence(a,n))
# } Driver Code Ends