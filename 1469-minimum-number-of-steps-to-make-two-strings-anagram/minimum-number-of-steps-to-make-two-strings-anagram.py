class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_dct=defaultdict(int)
        t_dct=defaultdict(int)
        for i in s:
            s_dct[i]+=1
        for i in t:
            t_dct[i]+=1
        ans=0
        for i in s_dct:
            if i not in t_dct:
                ans+=s_dct[i]
            else:
                if t_dct[i]<s_dct[i]:
                    ans+=s_dct[i]-t_dct[i]
                
        return ans