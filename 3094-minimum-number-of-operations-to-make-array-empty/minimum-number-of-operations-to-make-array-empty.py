class Solution:
    def minOperations(self, nums: List[int]) -> int:
        dct=Counter(nums)
        print(dct)
        ans=0
        for i in dct:
            while dct[i]>4:
                dct[i]-=3
                ans+=1
            if dct[i]%3==0:
                ans+=dct[i]//3
            elif dct[i]%2==0:
                ans+=dct[i]//2
            else:
                return -1
        return ans
        