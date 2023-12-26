class Solution:
    def __init__(self):
        self.mod=10**9+7

    def f(self,dice,face,target,dp):
        if dice==0:
            if target!=0:
                return 0
            else:
                return 1
        if target==0:
            if dice!=0:
                return 0
            else:
                return 1
        if (dice,target) in dp:
            return dp[(dice,target)]
        ans=0
        for i in range(1,face+1):
            ans+=self.f(dice-1,face,target-i,dp)
        dp[(dice,target)]=ans%(self.mod)
        return dp[(dice,target)]

    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        dp={}
        return self.f(n,k,target,dp)
        