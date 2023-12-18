class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        ans=[]
        i=0
        temp=[]
        for j in range(3,len(nums)+1,3):
            temp.append(nums[i:j])
            i=j
        for i in temp:
            if (i[2]-i[0])>k or (i[1]-i[0])>k or (i[2]-i[1])>k:
                return []
            ans.append(i)
        return ans
                
        