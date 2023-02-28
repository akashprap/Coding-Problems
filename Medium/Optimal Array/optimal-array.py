from typing import List


class Solution:
    def optimalArray(self, n : int, a : List[int]) -> List[int]:
        # code here
        ans =[0]
        sum1 = 0
        sum2 = 0
        for i in range(1,n):
            if((i+1)%2 == 0):
                sum1+=a[i//2]
                sum2+=a[i]
            else:
                sum2+=(a[i]-a[i//2])
            ans.append(sum2-sum1)
        return ans


#{ 
 # Driver Code Starts
class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        a=IntArray().Input(n)
        
        obj = Solution()
        res = obj.optimalArray(n, a)
        
        IntArray().Print(res)
        

# } Driver Code Ends