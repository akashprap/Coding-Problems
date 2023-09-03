class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        has=defaultdict(int)
        i=0
        cursum=0
        maxi=-float("inf")
        for ind,j in enumerate(nums):
            # print(maxi)
            has[j]+=1
            cursum+=j
            # print(cursum)
            if ind-i+1==k and len(has)>=m:
                maxi=max(maxi,cursum)
                continue
            while ind-i+1>k:
                cursum-=nums[i]
                has[nums[i]]-=1
                if has[nums[i]]==0:
                    del has[nums[i]]
                i+=1
                # print(i)
            if len(has)>=m:
                maxi=max(maxi,cursum)
        if len(has)>=m:
            maxi=max(maxi,cursum)
        if maxi==-float("inf"):
            return 0
        return maxi
                
                
            
                