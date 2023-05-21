#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def findMoves(self,n,chairs,p):
        #code here
        ans=0
        chairs.sort()
        p.sort()
        for i,j in zip(chairs,p):
            ans+=abs(i-j)
        return ans
        

#{ 
 # Driver Code Starts.
if __name__=="__main__":
    for _ in range(int(input())):
        n=int(input())
        a=[int(i) for i in input().split()]
        b=[int(i) for i in input().split()]
        obj=Solution()
        print(obj.findMoves(n,a,b))
        
# } Driver Code Ends