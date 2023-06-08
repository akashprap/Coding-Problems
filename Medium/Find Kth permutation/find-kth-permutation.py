#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
from typing import List
import math

class Solution:
    def kthPermutation(self, n : int, k : int) -> str:
        # code here
        numbers=[i for i in range(1,n+1)]
        fact=math.factorial(n-1)        
        ans=""
        k-=1
        while True:
            ans=ans+str(numbers[k//fact])
            numbers.pop(k//fact)
            if len(numbers)==0:
                break
            k=k%fact
            fact=fact//len(numbers)
        return ans
        


#{ 
 # Driver Code Starts.
if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        N, K = map(int, input().split())
        
        obj = Solution()
        res = obj.kthPermutation(N, K)
        
        print(res)
        

# } Driver Code Ends