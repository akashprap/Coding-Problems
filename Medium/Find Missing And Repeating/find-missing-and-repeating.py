#User function Template for python3

class Solution:
    def findTwoElement( self,arr, n): 
        # code here
        xor1=arr[0]
        for i in range(1,n):
            xor1=xor1^arr[i]
        for i in range(1,n+1):
            xor1=xor1^i
        set_bit=0
        set_bit=xor1 & ~(xor1 - 1)
        x=0
        y=0
        for i in range(n):
            if set_bit&arr[i]:
                x=x^arr[i]
            else:
                y=y^arr[i]
        for i in range(1,n+1):
            if set_bit & i:
                x=x^i
            else:
                y=y^i
        x_count = 0
        for i in range(n):
            if arr[i] == x:
                x_count += 1
        if x_count == 0:
            return [y, x]
        return [x, y]
        
        
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 

    tc=int(input())
    while tc > 0:
        n=int(input())
        arr=list(map(int, input().strip().split()))
        ob = Solution()
        ans=ob.findTwoElement(arr, n)
        print(str(ans[0])+" "+str(ans[1]))
        tc=tc-1
# } Driver Code Ends