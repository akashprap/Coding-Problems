#User function Template for python3

class Solution:
    def minOperations(self, n):
        # Code here
        no=n//2
        if n%2==0:
            return no**2
        else:
            return no*(no+1)
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    
    T = int(input())
    while T > 0: 
        N =int(input())
        ob = Solution()
        print(ob.minOperations(N))
        
        T -= 1

# } Driver Code Ends