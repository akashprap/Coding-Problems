#User function Template for python3

class Solution():
    def maxWeightCell(self, N, Edge):
        #your code goes here
        temp=[0]*N
        for i in range(N):
            if Edge[i]==-1:
                continue
            else:
                temp[Edge[i]]+=i
        maxi=max_ind=-1
        for i in range(N):
            if temp[i]>=maxi:
                maxi=temp[i]
                max_ind=i
        return max_ind


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        N = int(input())
        Edge = [int(i) for i in input().split()]
        obj = Solution()
        ans=obj.maxWeightCell(N, Edge);
        print(ans)

# } Driver Code Ends