#User function Template for python3
from collections import defaultdict
import heapq
class Solution:
    def shortestPath(self, n, m, edges):
        # Code here
        adj=defaultdict(list)
        for s,e,w in edges:
            adj[s].append((e,w))
            adj[e].append((s,w))#(node,edgeweight)
        dist=[1e9]*(n+1)
        # parent=[0]*(n+1)
        parent=[i for i in range(1,n+1)]
        parent.insert(0,0)
        dist[1]=0
        pq=[]
        heapq.heapify(pq)
        heapq.heappush(pq,(0,1))
        # pq.append((0,1))#(dist,node)
        while pq:
            dis,node=heapq.heappop(pq)
            for it in adj[node]:
                adjnode=it[0]
                edw=it[1]
                if dist[adjnode]>dis+edw:
                    dist[adjnode]=dis+edw
                    parent[adjnode]=node
                    heapq.heappush(pq,(dist[adjnode],adjnode))
        if dist[n]==1e9:
            return [-1]
        else:
            path=[]
            node=n
            while parent[node]!=node:
                path.append(node)
                node=parent[node]
            path.append(1)
            path.reverse()
            return path
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        n, m = list(map(int, input().split()))
        edges = []
        for i in range(m):
            node1, node2, weight = list(map(int, input().split()))
            edges.append([node1, node2, weight])
        obj = Solution()
        ans = obj.shortestPath(n, m, edges)
        for e in ans:
            print(e, end = ' ')
        print()
# } Driver Code Ends