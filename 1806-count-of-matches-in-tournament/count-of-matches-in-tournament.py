class Solution:
    def numberOfMatches(self, n: int) -> int:
        ans=0
        while n!=1:
            if n%2==1:
                ans+=(n-1)//2
                n=1+(n-1)//2
            else:
                ans+=n//2
                n=n//2
        return ans
        