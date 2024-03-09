class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        c=Counter(nums)
        maxi=0
        for i in c:
            maxi=max(maxi,c[i])
        ans=0
        for i in c:
            if c[i]==maxi:
                ans+=c[i]
        return ans