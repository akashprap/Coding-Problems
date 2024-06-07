class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s=0
        maxsum = nums[0]
        for i in nums:
            s+=i
            maxsum = max(maxsum,s)
            s = max(s,0)
        return maxsum