class Solution:
    def f(self,i,s,dset,dp):
        if i==len(s):
            return 0
        if i in dp:
            return dp[i]
        # ans=float('inf')
        ans=1+self.f(i+1,s,dset,dp)
        for j in range(i,len(s)):
            if s[i:j+1] in dset:
                ans=min(ans,self.f(j+1,s,dset,dp))
        dp[i]=ans
        return ans
    def minExtraChar(self, s: str, dic: List[str]) -> int:
        return self.f(0,s,set(dic),{})