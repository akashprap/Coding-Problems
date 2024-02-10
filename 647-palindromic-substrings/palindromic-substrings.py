class Solution:
    def countSubstrings(self, s: str) -> int:
        ans=0
        for i in range(len(s)):
            l,r=i,i
            while l>=0 and r<len(s) and s[l]==s[r]:
                ans+=1
                l-=1
                r+=1
            if i<len(s)-1:
                l=i
                r=i+1
                while l>=0 and r<len(s) and s[l]==s[r]:
                    ans+=1
                    l-=1
                    r+=1
        return ans
