class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:
        ans=0
        # curr=0
        seen=set()
        # temp=[]
        for i in range(1,target+1):
            if i not in seen:
                ans+=i
                n-=1
                if n==0:
                    return ans
                seen.add(i)
                seen.add(target-i)
        j=1
        while n:
            ans+=(target+j)
            n-=1
            j+=1
        return ans
        