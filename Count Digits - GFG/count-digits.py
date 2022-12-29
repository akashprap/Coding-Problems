#User function Template for python3


class Solution:
    def evenlyDivides (self, N):
        # code here
        temp=N
        ans=0
        while N:
            if N%10==0:
                N=N//10
            elif temp%(N%10)==0:
                ans+=1
                N=N//10
            else:
                N=N//10
        return ans
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print(ob.evenlyDivides(N))
# } Driver Code Ends