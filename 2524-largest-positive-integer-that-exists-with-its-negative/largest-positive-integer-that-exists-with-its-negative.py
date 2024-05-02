class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        maxi = -1
        ss = set(nums)
        for i in nums:
            if -i in ss:
                maxi=max(maxi,i)
        return maxi
            