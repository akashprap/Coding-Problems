class Solution:
    def countHomogenous(self, s: str) -> int:
        ans=0
        c=1
        mod=10**9+7
        for i in range(1,len(s)):
            if s[i]==s[i-1]:
                c+=1
            else:
                ans+=(c*(c+1))//2
                ans%=mod
                c=1
        ans+=(c*(c+1))//2
        ans%=mod
        return ans
