from typing import List


class Solution:
    def dominantPairs(self, n : int, arr : List[int]) -> int:
        # code here
        Larr = arr[:n//2]
        Rarr = arr[n//2:]
        Larr.sort()
        Rarr.sort()
        
        count = 0
        i,j = n//2-1,n//2-1
        while(i>=0 and j>=0):
            if(Larr[i]>=5*Rarr[j]):
                count+=(j+1)
                i-=1
            else:
                j-=1
        return count
        



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
        
        
        arr=IntArray().Input(n)
        
        obj = Solution()
        res = obj.dominantPairs(n, arr)
        
        print(res)
        

# } Driver Code Ends