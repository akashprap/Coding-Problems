class Solution:
    def largestOddNumber(self, num: str) -> str:
        for j in range(len(num)-1,-1,-1):
            if int(num[j])%2==1:
                return num[:j+1]
        return ""
        