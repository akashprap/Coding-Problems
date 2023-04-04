#User function Template for python3
from collections import defaultdict,deque
class Solution:
    def shortestPath(self, edges, n, m, src):
        # code here
        adj=defaultdict(list)
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        q=deque()
        q.append((src,0))
        dist=[float('inf') for i in range(n)]
        dist[src]=0
        while q:
            node,wt=q.pop()
            for neigh in adj[node]:
                if dist[neigh]>dist[node]+1:
                    dist[neigh]=dist[node]+1
                    q.append((neigh,wt+1))
        for i in range(n):
            if dist[i]==float('inf'):
                dist[i]=-1
        return dist


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, m = map(int, input().strip().split())
        edges=[]
        for i in range(m):
            li=list(map(int,input().split()))
            edges.append(li)
        src=int(input())
        ob = Solution()
        ans = ob.shortestPath(edges,n,m,src)
        for i in ans:
            print(i,end=" ")
        print()
        tc -= 1
# } Driver Code Ends