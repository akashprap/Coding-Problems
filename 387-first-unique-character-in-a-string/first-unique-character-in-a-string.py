class Solution:
    def firstUniqChar(self, s: str) -> int:
        cc=Counter(s)
        for i,_ in enumerate(s):
            if cc[_]==1:
                return i 
        return -1
        