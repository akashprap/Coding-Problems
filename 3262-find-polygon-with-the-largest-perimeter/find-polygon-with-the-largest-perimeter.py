class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        pref_sum=[nums[0]]
        for i in nums[1:]:
            pref_sum.append(i+pref_sum[-1])
        ans=-1
        for i in range(2,len(nums)):
            if pref_sum[i-1]>nums[i]:
                ans=pref_sum[i]
                
        return ans