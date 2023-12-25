class Solution:
    @cache
    def f(self,ind,s):
        if ind==-1:
            return 1
        ans=0
        if s[ind]!="0":
            ans+=self.f(ind-1,s)
        
        if ind>=1:
            if 10<=int(s[ind-1]+s[ind])<=26:
                ans+=self.f(ind-2,s)
        return ans
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        if s[0]=="0":
            return 0
        return self.f(len(s)-1,s)
                

        