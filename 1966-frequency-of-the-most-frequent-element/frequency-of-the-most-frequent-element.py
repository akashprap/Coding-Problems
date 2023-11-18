class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        presum=0
        i=0
        maxi=0
        for j in range(len(nums)):
            presum+=nums[j]
            while nums[j]*(j-i+1)>presum+k:
                presum-=nums[i]
                i+=1
            maxi=max(maxi,j-i+1)
        return maxi


        