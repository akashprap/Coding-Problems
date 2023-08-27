class Solution:
    def canCross(self, stones: List[int]) -> bool:
        stone=set()
        dp={}
        for i in stones:
            stone.add(i)
        def f(curr,k):
            if curr==stones[-1]:
                return True
            if (curr,k) in dp:
                return dp[(curr,k)]
            for jump in [k-1,k,k+1]:
                if jump>0 and (curr+jump) in stone:
                    if f(curr+jump,jump):
                        dp[(curr,k)]= True
                        return dp[(curr,k)]
            dp[(curr,k)]= False
            return dp[(curr,k)]




        return f(0,0)