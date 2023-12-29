class Solution:
    def minDifficulty(self, A, d):
        n = len(A)
        if n < d: return -1
        dp={}
        def f(ind,day,dp):
            if day==1:
                return max(A[ind:])
            if (ind,day) in dp:
                return dp[(ind,day)]
            currmax=0
            res=float("inf")
            for i in range(ind,n-day+1):
                currmax=max(currmax,A[i])
                res=min(res,currmax+f(i+1,day-1,dp))
            dp[(ind,day)]=res
            return res
        return f(0,d,dp)
