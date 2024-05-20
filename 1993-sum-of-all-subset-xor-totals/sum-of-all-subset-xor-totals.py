class Solution:
    def get_subset(self,nums,arr,ind,temp):
        if ind == len(nums):
            arr.append(temp.copy())
            return
        temp.append(nums[ind])
        self.get_subset(nums,arr,ind+1,temp)
        temp.pop()
        self.get_subset(nums,arr,ind+1,temp)

    def get_xor_from_array(self,nums):
        if not nums:
            return 0
        else:
            xorr = nums[0]
            for num in nums[1:]:
                xorr^=num
            return xorr

    def subsetXORSum(self, nums: List[int]) -> int:
        arr= []
        self.get_subset(nums,arr,0,[])
        ans = 0
        for ar in arr:
            ans+=self.get_xor_from_array(ar)       
        return ans