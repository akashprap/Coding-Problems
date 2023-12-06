class Solution:
    def totalMoney(self, n: int) -> int:
        weeks=n//7
        ans=0
        ww=0
        if n>7:
            for i in range(weeks+1):
                ww+=1
                for j in range(ww,ww+min(n,7)):
                    ans+=j
                n-=7
            return ans
        else:
            return (n*(n+1))//2


        