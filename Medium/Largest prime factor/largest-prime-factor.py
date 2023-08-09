#User function Template for python3
import math
class Solution:
    def largestPrimeFactor (self, N):
        # code here
        maxi=-1
        while N%2==0:
            maxi=2
            N=N//2
        for i in range(3, int(math.sqrt(N)) + 1, 2):
            while N%i==0:
                maxi=i
                N=N//i
        if N>2:
            return N
        return maxi


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print(ob.largestPrimeFactor(N))
# } Driver Code Ends