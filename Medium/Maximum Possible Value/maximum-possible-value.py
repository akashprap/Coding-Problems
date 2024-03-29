#User function Template for python3
class Solution:
    def maxPossibleValue(self, N, A, B):

        mn=int(1e9)

        count=0

        res=0

        for i in range(N):

            if B[i]>1:

                rect_pairs=B[i]//2

                res+=2*(rect_pairs*A[i])

                mn=min(mn,A[i])

                count+=rect_pairs

        if count%2!=0:

            res-=2*mn

        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input().strip())
        A = list(map(int, input().strip().split()))
        B = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maxPossibleValue(N, A, B)
        print(ans)

# } Driver Code Ends