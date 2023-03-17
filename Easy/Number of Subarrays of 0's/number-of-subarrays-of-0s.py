#User function Template for python3

class Solution():
    def no_of_subarrays(self, n,arr):
        #your code goes here
        ans=0
        c=0
        for i in range(n):
            if arr[i]==0:
                c+=1
            else:
                ans+=(c*(c+1))//2
                c=0
        ans+=(c*(c+1))//2
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3


for _ in range(int(input())):
    n = int(input())
    arr = [int(i) for i in input().split()]
    print(Solution().no_of_subarrays(n, arr))
# } Driver Code Ends