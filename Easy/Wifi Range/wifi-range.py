#User function Template for python3
class Solution:
    def wifiRange(self, N, S, X): 
        count = 0
        for i in range(N):
            if S[i] == '1':
                count = X
            else:
                count -= 1
            if count < -X:
                return False
        if count < 0:
            return False
        return True



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N,X = map(int,input().strip().split())
        S = input()
        ob = Solution()
        ans = ob.wifiRange(N, S, X)
        if ans:
            print(1)
        else:
            print(0)

# } Driver Code Ends