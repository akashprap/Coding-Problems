class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s=s.lower()
        vow='aeiou'
        c1,c2=0,0
        n=len(s)
        for i in range(n//2):
            if s[i] in vow:
                c1+=1
        for j in range(n//2,n):
            if s[j] in vow:
                c2+=1
        return c1==c2