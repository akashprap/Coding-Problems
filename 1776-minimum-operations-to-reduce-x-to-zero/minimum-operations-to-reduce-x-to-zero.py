class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target=sum(nums)-x
        n=len(nums)
        if x>sum(nums):
            return -1
        elif x==sum(nums):
            return n
        else:
            #find target in subarray using prefix sum
            cursum=0
            maxi=0
            i=0
            for j in range(len(nums)):
                cursum+=nums[j]
                while cursum>target:
                    cursum-=nums[i]
                    i+=1
                if cursum==target:
                    maxi=max(maxi, (j-i+1))
            if maxi:
                return n-maxi

            return -1
