#User function Template for python3
class Solution:
    def minIncrements(self, arr, N): 
        arr.sort()
        increments = 0
        for i in range(1, N):
            if arr[i] <= arr[i-1]:
                increments += (arr[i-1] - arr[i] + 1)
                arr[i] = arr[i-1] + 1
        return increments


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    
    T = int(input())
    while T > 0: 
        N=int(input())
        arr = [int(i) for i in input().split()]
        ob = Solution()
        print(ob.minIncrements(arr,N))
        
        T -= 1
# } Driver Code Ends