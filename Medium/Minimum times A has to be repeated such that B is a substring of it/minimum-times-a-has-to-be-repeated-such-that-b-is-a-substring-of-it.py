#User function Template for python3

class Solution:
    def minRepeats(self, A, B):
        # code here 
        limit=len(B)//len(A)
        c=0
        ans=""
        for i in range(limit+2):
            if B in ans:
                return c
            else:
                ans+=A
                c+=1
        return -1
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        A=input()
        B=input()
        
        ob = Solution()
        print(ob.minRepeats(A,B))
# } Driver Code Ends