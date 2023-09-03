class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        c1=defaultdict(int)        
        c2=defaultdict(int)
        for i in range(len(s)):
            c1[s[i]]+=1
            c2[t[i]]+=1
            c11=[]
            c22=[]
            for _ in c1:
                c11.append(c1[_])
            for _ in c2:
                c22.append(c2[_])
            if c11!=c22:
                return False
        return True

        