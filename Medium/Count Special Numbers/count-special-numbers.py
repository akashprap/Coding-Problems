#User function Template for python3

class Solution:
    def countSpecialNumbers(self, N, arr):
        # Code here
        m=max(arr)
        sieve=[0]*(m+1)
        for i in arr:
            if sieve[i]<=1:
                for j in range(i,m+1,i):
                    sieve[j]+=1
        # print(sieve)
        ans=0
        for i in arr:
            if sieve[i]>1:
                ans+=1
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    
    T = int(input())
    while T > 0: 
        N=int(input())
        arr = [int(i) for i in input().split()]
        ob = Solution()
        print(ob.countSpecialNumbers(N, arr))
        
        T -= 1
# } Driver Code Ends