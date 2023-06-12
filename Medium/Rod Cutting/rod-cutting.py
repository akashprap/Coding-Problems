#User function Template for python3
import sys
class Solution:
    # def f(self,ind,n,price,dp):
    #     if ind==0:
    #         return price[ind]*n
    #     if dp[ind][n]!=-1:
    #         return dp[ind][n]
            
    #     nottake=0+self.f(ind-1,n,price,dp)
    #     rodlength=ind+1
    #     take=-sys.maxsize-1
    #     if rodlength<=n:
    #         take=price[ind]+self.f(ind,n-rodlength,price,dp)
    #     dp[ind][n]= max(take,nottake)
    #     return dp[ind][n]
            
    def cutRod(self, price, n):
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            for j in range(i):
                dp[i] = max(dp[i], price[j] + dp[i - j - 1])
        return dp[n]
    

                
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.cutRod(a, n))

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends