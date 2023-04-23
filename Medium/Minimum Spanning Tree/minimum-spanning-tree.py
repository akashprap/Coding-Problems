#User function Template for python3
from heapq import heappop,heappush,heapify
class Solution:
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        #code here
        vis=[0]*V
        pq=[]
        heapify(pq)
        pq.append((0,0))
        s=0
        while pq:
            wt,node=heappop(pq)
            if vis[node]:
                continue
            else:
                vis[node]=1
                s+=wt
                for adjnode,edw in adj[node]:
                    if vis[adjnode]==0:
                        heappush(pq,(edw,adjnode))
        return s
                        
                        


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