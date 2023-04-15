#User function Template for python3
import heapq
class Solution:
        
    def MinimumEffort(self, arr):
        #code here
        n=len(arr)
        m=len(arr[0])
        dist=[[float("inf")]*m for i in range(n)]
        dist[0][0]=0
        pq=[]
        pq.append((0,(0,0)))
        heapq.heapify(pq)
        while pq:
            it=heapq.heappop(pq)
            dis=it[0]
            r=it[1][0]
            c=it[1][1]
            if r==n-1 and c==m-1:
                return dis
            dz=[-1,0,1,0,-1]
            for i in range(4):
                nr=r+dz[i]
                nc=c+dz[i+1]
                if nr>=0 and nr<n and nc>=0 and nc<m:
                    neweffort=max(dis,abs(arr[r][c]-arr[nr][nc]))
                    if neweffort<dist[nr][nc]:
                        dist[nr][nc]=neweffort
                        heapq.heappush(pq,(neweffort,(nr,nc)))
        return 0


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n,m=map(int,input().split())
        a=[]
        for i in range(n):
            li=list(map(int,input().split()))
            a.append(li)
        ob = Solution()
        ans = ob.MinimumEffort(a)
        print(ans)
        tc -= 1
# } Driver Code Ends