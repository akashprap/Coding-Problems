#User function Template for python3

class Solution:
    def reversedBits(self, X):
        # code here 
        ans=(32-len(bin(X)[2:]))*"0"+str(bin(X)[2:])
        ans=ans[::-1]
        return int(ans,2)
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        X=int(input())
        
        ob = Solution()
        print(ob.reversedBits(X))
# } Driver Code Ends