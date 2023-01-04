from typing import List

from bisect import bisect_left

 

class Solution:

    def maximum_profit(self, n : int, intervals : List[List[int]]) -> int:

        # code here

        

        intervals.sort()

        dp =[0]*(n+1)

        

        for i in range(n-1, -1, -1):

            s, e, p = intervals[i]

            j = bisect_left(intervals,[e, e, 0])

            dp[i] = max(dp[i+1], dp[j] + p)

            

        return dp[0]



#{ 
 # Driver Code Starts
class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        intervals=IntMatrix().Input(n, 3)
        
        obj = Solution()
        res = obj.maximum_profit(n, intervals)
        
        print(res)
        

# } Driver Code Ends