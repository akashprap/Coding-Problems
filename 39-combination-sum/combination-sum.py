class Solution:
    def f(self,ind,n,c,t,temp,res):
        if ind==n:
            if t==0:
                res.append(temp.copy())
            return
        if t==0:
            res.append(temp.copy())
            return
        if t<0:
            return
        
        if c[ind]<=t:
            temp.append(c[ind])
            self.f(ind,n,c,t-c[ind],temp,res)
            temp.pop()
        self.f(ind+1,n,c,t,temp,res)

    def combinationSum(self, c: List[int], t: int) -> List[List[int]]:
        res=[]
        n=len(c)
        temp=[]
        self.f(0,n,c,t,temp,res)
        return res