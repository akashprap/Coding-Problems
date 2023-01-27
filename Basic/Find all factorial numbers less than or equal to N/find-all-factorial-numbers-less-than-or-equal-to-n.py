#User function Template for python3

class Solution:
    def f(self,i,N,arr,fact):
        if fact>N:
            return
        arr.append(fact)
            
        self.f(i+1,N,arr,fact*i)
    def factorialNumbers(self, N):
    	#code here 
    	arr=[]
    	self.f(2,N,arr,1)
    	return arr


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.factorialNumbers(N)
        for i in ans:
            print(i, end=" ")
        print()
        
# } Driver Code Ends