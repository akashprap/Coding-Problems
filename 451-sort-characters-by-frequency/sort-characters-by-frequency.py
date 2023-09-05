import operator
class Solution:
    def frequencySort(self, s: str) -> str:
        d=defaultdict(int)
        for i in s:
            d[i]+=1
        maxheap=[]
        heapify(maxheap)
        for i in d:
            heappush(maxheap,(-d[i],i))
        # sorted_d = dict( sorted(d.items(), key=operator.itemgetter(1),reverse=True))
        #print()
        ans=""
        while maxheap:
            maxi=heappop(maxheap)
            ans+=(-maxi[0]*maxi[1])
        return ans