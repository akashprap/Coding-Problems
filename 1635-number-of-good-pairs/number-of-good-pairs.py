class Solution:
    def calc(self,n):
        if n>1:
            return (n*(n-1))//2
        else:
            return 0
    def numIdenticalPairs(self, nums: List[int]) -> int:
        c=Counter(nums)
        ans=0
        for i in c:
            ans+=self.calc(c[i])
        return ans
        