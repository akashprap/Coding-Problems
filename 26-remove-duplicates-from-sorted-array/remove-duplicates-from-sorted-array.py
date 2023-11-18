class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k=len(set(nums))
        f=nums[0]
        ind=1
        for i in range(1,len(nums)):
            if nums[i]==f:
                continue
            else:
                nums[ind]=nums[i]
                f=nums[i]
                ind+=1
        # nums[ind]=f
        return k

