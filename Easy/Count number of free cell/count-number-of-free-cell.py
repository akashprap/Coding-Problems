#User function Template for python3

class Solution():
    def countZero(self, n, k ,arr):
        #your code here
        row=set()
        col=set()
        ans=[]
        for i,j in arr:
            row.add(i)
            col.add(j)
            ans.append((n-len(row))*(n-len(col)))
        return ans
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3


for _ in range(int(input())):
    n,k=map(int,input().split())
    arr = []
    for i in range(k):
        x,y=map(int,input().split())
        arr.append([x, y])
    obj = Solution()
    res = obj.countZero(n, k, arr)
    for i in res:
        print(i,end = " ")
    print()
# } Driver Code Ends