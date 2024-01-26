class Solution:
    def __init__(self):
        self.mod=10**9+7
    def f(self,i,j,maxmove,m,n,dp):
        if maxmove<0:
            return 0
        if i<0 or i>=m or j<0 or j>=n:
            return 1
        if (i,j,maxmove) in dp:
            return dp[(i,j,maxmove)]
        ans=self.f(i-1,j,maxmove-1,m,n,dp)+self.f(i,j-1,maxmove-1,m,n,dp)+self.f(i+1,j,maxmove-1,m,n,dp)+self.f(i,j+1,maxmove-1,m,n,dp)
        dp[(i,j,maxmove)]= ans%self.mod
        return dp[(i,j,maxmove)]
    def findPaths(self, m: int, n: int, maxMove: int, sr: int, sc: int) -> int:
        dp={}
        return self.f(sr,sc,maxMove,m,n,dp)
        