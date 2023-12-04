class Solution:
    def largestGoodInteger(self, num: str) -> str:
        ans=""
        f=0
        maxi=000
        for i in range(10):
            ans=str(i)*3
            if ans in num:
                maxi=ans
                f=1
        if f==0:
            return ""
        return str(maxi) 

                    


        