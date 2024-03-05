class Solution:
    def minimumLength(self, s: str) -> int:
        i=0
        j=len(s)-1
        while i<j and s[i]==s[j]:
            curr = s[i]
            while i<=j and s[i]==curr:
                i+=1
            while j>=i and s[j]==curr:
                j-=1
        return j-i+1