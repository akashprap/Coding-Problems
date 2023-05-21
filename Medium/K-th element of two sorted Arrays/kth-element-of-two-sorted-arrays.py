#User function Template for python3
import sys
class Solution:
    def kthElement(self,  arr1, arr2, n, m, k):
        A,B=arr1,arr2
        if n>m:
            A,B=B,A
            n,m=m,n
        # print(n,m)
        l=max(0,k-m)
        h=min(k,n)
        while l<=h:
            cut1=(l+h)//2
            cut2=k-cut1
            l1=-sys.maxsize-1 if cut1==0 else A[cut1-1]
            r1=sys.maxsize if cut1==n else A[cut1]
            l2=-sys.maxsize-1 if cut2==0 else B[cut2-1]
            r2=sys.maxsize if cut2==m else B[cut2]
            
            if l1<=r2 and l2<=r1:
                return max(l1,l2)
            elif l1>r2:
                h=cut1-1
            else:
                l=cut1+1
        
                
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        sz = [int(x) for x in input().strip().split()]
        n, m, k = sz[0], sz[1], sz[2]
        a = [int(x) for x in input().strip().split()]
        b = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.kthElement( a, b, n, m, k))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends