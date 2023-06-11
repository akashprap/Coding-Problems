#User function Template for python3

class Solution:
    def update(self, a, n, updates, k):
        # Your code goes here
        temp=[0]*n
        for i in updates:
            temp[i-1]+=1
        for i in range(n):
            if i==0:
                a[i]=temp[i]
            else:
                a[i]=a[i-1]+temp[i]
        return a



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    T = int(input())

    while(T > 0):
        sz = [int(x) for x in input().strip().split()]
        n , k = sz[0] , sz[1]
        a = [0 for i in range(n)]
        updates = [int(x) for x in input().strip().split()]
        ob=Solution()
        ob.update(a, n, updates, k)
        print(*a)

        T -= 1


# } Driver Code Ends