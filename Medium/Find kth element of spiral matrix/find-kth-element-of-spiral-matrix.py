#User function Template for python3

class Solution:
    def findK(self, a, n, m, k):
        # Write Your Code here
        lcol=0
        rcol=m-1
        topr=0
        botr=n-1
        while topr<=botr and lcol<=rcol:
            for i in range(lcol,rcol+1):
                k-=1
                if k==0:
                    return a[topr][i]
            topr+=1
            for j in range(topr,botr+1):
                k-=1
                if k==0:
                    return a[j][rcol]
            rcol-=1
            if topr<=botr:
                for i in range(rcol,lcol-1,-1):
                    k-=1
                    if k==0:
                        return a[botr][i]
                botr-=1
            if lcol<=rcol:
                for j in range(botr,topr-1,-1):
                    k-=1
                    if k==0:
                        return a[j][lcol]
                lcol+=1
        return -1

#{ 
 # Driver Code Starts

#Initial Template for Python 3

for _ in range(int(input())):
    n, m, k = map(int,input().split())
    a = [
            list(map(int,input().split()))
            for _ in range(n)
        ]
    
    ob = Solution()
    print(ob.findK(a,n,m,k))
    
# } Driver Code Ends