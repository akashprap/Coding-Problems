class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        dct=defaultdict(list)
        for ind,val in enumerate(s):
            dct[val].append(ind)
        maxi=-1
        for i in dct:
            if len(dct[i])>=2:
                maxi=max(maxi,dct[i][-1]-dct[i][0]-1)
        return maxi
        