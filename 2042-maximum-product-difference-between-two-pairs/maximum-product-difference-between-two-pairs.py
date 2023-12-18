class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        maxheap=[]
        minheap=[]
        for i in nums:
            heappush(maxheap,-i)
            heappush(minheap,i)
        return (heappop(maxheap)*heappop(maxheap))-(heappop(minheap)*heappop(minheap))