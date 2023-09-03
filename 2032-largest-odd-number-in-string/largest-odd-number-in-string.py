class Solution:
    def largestOddNumber(self, nums: str) -> str:
        ans=""
        for i in nums[::-1]:
            if int(i)%2==1:
                ans+=i
            else:
                if ans=="":
                    continue
                else:
                    ans+=i
        if ans=="":
            return ""
        return (ans)[::-1]