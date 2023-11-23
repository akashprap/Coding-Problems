class Solution:
    def check(self,arr):
        if len(arr)<=2:
            return True
        else:
            arr.sort()
            diff=arr[1]-arr[0]
            for i in range(2,len(arr)):
                if arr[i]-arr[i-1]!=diff:
                    return False
            return True
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans=[]
        for i,j in zip(l,r):
            ans.append(self.check(nums[i:j+1]))
        return ans


        