#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
class Solution:
    def countSubstring(self, S): 
        #code here
        N=len(S)
        ans=0
        for i in range(N):
            sm=0
            la=0
            for j in range(i,N):
                if ord(S[j])>=65  and ord(S[j])<=91:
                    la+=1
                else:
                    sm+=1
                if la==sm:
                    ans+=1
                else:
                    continue
        return ans
                

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        S = input()
        ob = Solution()
        ans = ob.countSubstring(S)
        print(ans)

# } Driver Code Ends