class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos=[]
        neg=[]
        for i in nums:
            if i<0:
                neg.append(i)
            else:
                pos.append(i)
        i=0
        j=0
        k=0
        while i<len(pos) and j<len(neg):
            nums[k]=pos[i]
            k+=1
            i+=1
            nums[k]=neg[j]
            k+=1
            j+=1
        return nums