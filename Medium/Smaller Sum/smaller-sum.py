from typing import List
from collections import defaultdict

class Solution:
    
    def smallerSum(self, n : int, arr : List[int]) -> List[int]:
        hashmap = {}
        ans = []
        arrcpy = arr.copy()
        
        arrcpy.sort()
        
        prefixSum = arrcpy[0]
        hashmap[arrcpy[0]] = 0
        
        for i in range(1, n):
            if arrcpy[i-1] == arrcpy[i]:
                sum = hashmap[arrcpy[i-1]]
                hashmap[arrcpy[i]] = sum
            else:
                hashmap[arrcpy[i]] = prefixSum
            
            prefixSum += arrcpy[i]
        
        for i in range(n):
            ans.append(hashmap[arr[i]])
        
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
        
        
        arr=IntArray().Input(n)
        
        obj = Solution()
        res = obj.smallerSum(n, arr)
        
        IntArray().Print(res)
        

# } Driver Code Ends