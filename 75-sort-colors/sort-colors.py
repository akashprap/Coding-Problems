class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l=0
        m=0
        h=len(nums)-1
        while m<=h:
            if nums[m]==0:
                nums[l],nums[m]=nums[m],nums[l]
                l+=1
                m+=1
            elif nums[m] == 2:
                nums[h],nums[m] = nums[m],nums[h]
                h-=1
            else:
                m+=1
            # print(nums)