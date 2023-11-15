class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        if len(arr)==1: return 1
        ans=1
        maxi=1
        for i in range(1,len(arr)):
            if (arr[i] - ans)> 1:
                ans+=1
            else:
                ans=arr[i]
                maxi=max(maxi,arr[i])
        return ans