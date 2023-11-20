class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        ans=0
        for i in garbage:
            ans+=len(i)
        presum=[travel[0]]
        for i in travel[1:]:
            presum.append(presum[-1]+i)
        maxm=0
        maxp=0
        maxg=0
        for ind,val in enumerate(garbage):
            if "P" in val:
                maxp=ind
            if "G" in val:
                maxg=ind
            if "M" in val:
                maxm=ind
        if maxg!=0:
            ans+=presum[maxg-1]
        if maxp!=0:
            ans+=presum[maxp-1]
        if maxm!=0:
            ans+=presum[maxm-1]
        return ans

        