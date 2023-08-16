
class Solution:
    def solve(self,n,k):
        res=1
        # (10 C 5)
        # 10*9*8*7*6/5*4*3*2*1
        for i in range(k):
            res = res * (n - i)
            res = res // (i + 1)
        return res
    def findCatalan(self, n : int) -> int:
        # code here
        ans=0
        if n<=1:
            ans=1
        ans= self.solve(2*n,n)
        # print(ans)
        return (ans//(n+1))%(10**9+7)

#{ 
 # Driver Code Starts
if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        obj = Solution()
        res = obj.findCatalan(n)
        
        print(res)
        

# } Driver Code Ends