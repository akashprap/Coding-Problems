import operator
class Solution:
    def frequencySort(self, s: str) -> str:
        d=defaultdict(int)
        for i in s:
            d[i]+=1
        sorted_d = dict( sorted(d.items(), key=operator.itemgetter(1),reverse=True))
        #print()
        ans=""
        for i in sorted_d:
            ans+=i*d[i]
        return ans