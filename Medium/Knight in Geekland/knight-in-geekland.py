#User function Template for python3
from collections import deque

class Solution:
    def bfs(self,q,arr,start,al,vis):
        n=len(arr)
        m=len(arr[0])
        q.append(start)
        vis[start[0]][start[1]]=1
        dr=[-2,-1,1,2,2,1,-1,-2]
        dc=[1,2,2,1,-1,-2,-2,-1]
        while q:
            l=len(q)
            cusum=0
            for _ in range(l):
                node=q.popleft()
                # print(node)
                cusum+=arr[node[0]][node[1]]
                for i in range(8):
                    nr=node[0]+dr[i]
                    nc=node[1]+dc[i]
                    if nr>=0 and nr<n and nc>=0 and nc<m and vis[nr][nc]==0:
                        vis[nr][nc]=1
                        q.append([nr,nc])
                # print(cusum)
            al.append(cusum)
        # return al
                
                
        
        
    def knightInGeekland(self, arr, start):
        n=len(arr)
        m=len(arr[0])
        vis=[[0]*m for i in range(n)]
        q=deque()
        al=[]
        self.bfs(q,arr,start,al,vis)
        l=len(al)
        for i in range(l-1,-1,-1):
            if (al[i]+i)<l:
                al[i]+=al[al[i]+i]
        maxi=-1
        ind=-1
        for i in range(l):
            if  al[i]>maxi:
                maxi=al[i]
                ind=i
        return ind
        
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    test_cases = int(input())
    for _ in range (test_cases):
        n,m = map(int, input().split())
        starting_x, starting_y = map(int, input().split())
        orignal_array = []

        for i in range(n):
            l = list(map(int, input().split()))
            orignal_array.append(l)

        res = Solution().knightInGeekland(orignal_array, [starting_x, starting_y])
        print(res)
# } Driver Code Ends