#User function Template for python3

class Solution:

    def longestPalin(self, s):

        # code here

        if len(s)==1:

            return s

    

        for i in range(len(s),0,-1):

            for j in range(len(s)-i+1):

                x=s[j:i+j]

                if x==x[::-1]:
                    return x 




#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        S = input()

        ob = Solution()

        ans = ob.longestPalin(S)

        print(ans)
# } Driver Code Ends