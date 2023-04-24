#User function Template for python3
# from heapq import heappop,heappush,heapify
# class Solution:
    
#     #Function to find sum of weights of edges of the Minimum Spanning Tree.
#     def spanningTree(self, V, adj):
#         #code here
#         vis=[0]*V
#         pq=[]
#         heapify(pq)
#         pq.append((0,0))
#         s=0
#         while pq:
#             wt,node=heappop(pq)
#             if vis[node]:
#                 continue
#             else:
#                 vis[node]=1
#                 s+=wt
#                 for adjnode,edw in adj[node]:
#                     if vis[adjnode]==0:
#                         heappush(pq,(edw,adjnode))
#         return s
                        
class DisjointSet:
    def __init__(self, n):
        self.rank = [0] * (n + 1)
        self.parent = list(range(n + 1))
        self.size = [1] * (n + 1)

    def findUPar(self, node):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.findUPar(self.parent[node])
        return self.parent[node]

    def unionByRank(self, u, v):
        ulp_u = self.findUPar(u)
        ulp_v = self.findUPar(v)
        if ulp_u == ulp_v:
            return
        if self.rank[ulp_u] < self.rank[ulp_v]:
            self.parent[ulp_u] = ulp_v
        elif self.rank[ulp_v] < self.rank[ulp_u]:
            self.parent[ulp_v] = ulp_u
        else:
            self.parent[ulp_v] = ulp_u
            self.rank[ulp_u] += 1

    def unionBySize(self, u, v):
        ulp_u = self.findUPar(u)
        ulp_v = self.findUPar(v)
        if ulp_u == ulp_v:
            return
        if self.size[ulp_u] < self.size[ulp_v]:
            self.parent[ulp_u] = ulp_v
            self.size[ulp_v] += self.size[ulp_u]
        else:
            self.parent[ulp_v] = ulp_u
            self.size[ulp_u] += self.size[ulp_v]

class Solution:
    def spanningTree(self, V, adj):
        edges = []
        for i in range(V):
            for it in adj[i]:
                adjNode, wt = it[0], it[1]
                node = i
                edges.append((wt, (node, adjNode)))
        ds = DisjointSet(V)
        edges.sort()
        mstWt = 0
        for wt, (u, v) in edges:
            if ds.findUPar(u) != ds.findUPar(v):
                mstWt += wt
                ds.unionBySize(u, v)
        return mstWt                   


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        ob = Solution()
        
        print(ob.spanningTree(V,adj))
# } Driver Code Ends