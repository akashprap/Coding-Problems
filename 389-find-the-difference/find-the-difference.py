class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        z=( Counter(t)-Counter(s))
        for i in z :
            if z[i]>0:
                return i