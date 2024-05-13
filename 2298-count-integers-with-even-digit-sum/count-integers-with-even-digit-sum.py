class Solution:
    def countEven(self, num: int) -> int:
        count=0
        def suum(n):
            s=0
            while n:
                s+=n%10
                n=n//10
            return s%2==0
        for i in range(1,num+1):
            count+=1 if suum(i) else 0
        return count