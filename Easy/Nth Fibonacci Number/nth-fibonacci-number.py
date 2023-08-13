
class Solution:
    def nthFibonacci(self, n : int) -> int:
        # code here
        fib=[1]*n
        for i in range(2,n):
            fib[i]=(fib[i-1]+fib[i-2])%(10**9+7)
        # print(fib)
        return fib[n-1]%(10**9+7)
        



#{ 
 # Driver Code Starts
if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        obj = Solution()
        res = obj.nthFibonacci(n)
        
        print(res)
        

# } Driver Code Ends