
from typing import List


class Solution:
    def Rearrange(self, n : int, arr : List[int]) -> None:
        # code here
        i=0
        j=0
        while j<n:
            if arr[j]<0:
                ele=arr.pop(j)
                arr.insert(i,ele)
                i+=1
            j+=1
        return arr
            
        



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
        
        
        arr=IntArray().Input(2)
        
        obj = Solution()
        obj.Rearrange(n, arr)
        
        print(*arr, end=' ')
        print()

# } Driver Code Ends