class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref=[nums[0]]
        for i in nums[1:]:
            pref.append(i*pref[-1])
        suff=[nums[-1]]
        for i in nums[::-1][1:]:
            suff.append(suff[-1]*i)
        suff=suff[::-1]

        ans=[]
        for i in range(len(nums)):
            if i==0:
                ans.append(suff[i+1])
            elif i==len(nums)-1:
                ans.append(pref[i-1])
            else:
                ans.append(pref[i-1]*suff[i+1])
        return ans