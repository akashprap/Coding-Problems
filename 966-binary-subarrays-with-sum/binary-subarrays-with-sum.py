class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        dct=defaultdict(int)
        dct[0]=1
        ans=0
        i=0
        j=0
        curr=0
        for j in range(len(nums)):
            curr+=nums[j]
            ans+=dct[curr-goal]
            dct[curr]+=1
        return ans
